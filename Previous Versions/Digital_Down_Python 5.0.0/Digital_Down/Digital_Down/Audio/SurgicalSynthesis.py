import math
import os
import json
import shutil
from .AudioSampleValues import *
import numpy as np
import soundfile as sf
from pydub import AudioSegment
import sys
import glob
from .AudioNormalize import *
from .AudioProselyte import *
from .Waveforms import Waveforms

class OscillationExtraction:
    @staticmethod
    def fullphase(audio_data, channel=0, LowSamplePhaseCount=0, LSPCOperation='omit'):
        oscillations = []
        current_oscillation = []
        positive_count = 0
        negative_count = 0
        state = 'zero'
        
        print(f"Starting SFT with LowSamplePhaseCount={LowSamplePhaseCount}, LSPCOperation={LSPCOperation}")
        for i, sample in enumerate(audio_data):
            value = sample[channel]
            current_oscillation.append(value)

            if state == 'zero':
                if value > 0:
                    state = 'positive'
                    positive_count = 1
                elif value < 0:
                    state = 'negative'
                    negative_count = 1
            elif state == 'positive':
                if value > 0:
                    positive_count += 1
                elif value < 0:
                    state = 'negative'
                    negative_count = 1
            else:  # state == 'negative'
                if value < 0:
                    negative_count += 1
                elif value > 0:
                    # Check if we've completed a full oscillation
                    if positive_count > 0 and negative_count > 0:
                        if (positive_count <= LowSamplePhaseCount or negative_count <= LowSamplePhaseCount) and LSPCOperation == 'omit':
                            print(f"Omitting oscillation: positive_count={positive_count}, negative_count={negative_count}")
                            current_oscillation = [value]
                        else:
                            oscillations.append({
                                'samples': current_oscillation,
                                'positive_count': positive_count,
                                'negative_count': negative_count
                            })
                            print(f"Oscillation detected: positive_count={positive_count}, negative_count={negative_count}")
                            current_oscillation = [value]
                    
                    # Reset for the next oscillation
                    state = 'positive'
                    positive_count = 1
                    negative_count = 0

            if i % 10000 == 0:
                print(f"Processed {i} samples")

        # Add the last oscillation if it exists
        if current_oscillation:
            oscillations.append({
                'samples': current_oscillation,
                'positive_count': positive_count,
                'negative_count': negative_count
            })

        print(f"SFT completed. Total oscillations detected: {len(oscillations)}")
        return oscillations

    @staticmethod
    def singlephase(audio_data, channel=0, phase='positive', LowSamplePhaseCount=0, LSPCOperation='omit'):
        current_oscillation = []
        oscillations = []
        positive_count = 0
        negative_count = 0
        
        print(f"Starting SinglePhaseSFT with phase={phase}, LowSamplePhaseCount={LowSamplePhaseCount}, LSPCOperation={LSPCOperation}")

        for i, sample in enumerate(audio_data):
            value = sample[channel]

            if value > 0:
                positive_count += 1
                current_oscillation.append(value)
            elif value < 0:
                negative_count += 1
                current_oscillation.append(value)
            else:  # value == 0
                current_oscillation.append(value)

            # Check if we've completed a half oscillation
            if (phase == 'positive' and value <= 0 and positive_count > 0) or \
               (phase == 'negative' and value >= 0 and negative_count > 0):
                
                count_to_check = positive_count if phase == 'positive' else negative_count
                
                if count_to_check <= LowSamplePhaseCount:
                    print(f"Low {phase} count detected: {count_to_check}")
                    if LSPCOperation == 'omit':
                        print(f"Omitting low {phase} count samples")
                        current_oscillation = current_oscillation[:-count_to_check]
                        if phase == 'positive':
                            positive_count = 0
                        else:
                            negative_count = 0
                    elif LSPCOperation == 'ignore':
                        print(f"Ignoring low {phase} count")
                        # Do nothing, keep the samples but don't count them
                        if phase == 'positive':
                            positive_count = 0
                        else:
                            negative_count = 0
                
                if (phase == 'positive' and positive_count > 0) or (phase == 'negative' and negative_count > 0):
                    oscillations.append({
                        'samples': current_oscillation,
                        'positive_count': positive_count,
                        'negative_count': negative_count
                    })
                    print(f"Half oscillation detected: positive_count={positive_count}, negative_count={negative_count}")

                # Reset for the next oscillation
                positive_count = 0
                negative_count = 0
                current_oscillation = []

            if i % 10000 == 0:
                print(f"Processed {i} samples")

        print(f"SinglePhaseSFT completed. Total half oscillations detected: {len(oscillations)}")
        return oscillations


class SurgicalSynthesis:
    sample_rate = 44100
    note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    min_samples = sample_rate  # 1 second
    max_samples = sample_rate * 10  # 10 seconds
    @classmethod
    def get_next_part_number(cls, note_folder, note):
        existing_parts = [int(f.split('_')[1].split('.')[0]) for f in os.listdir(note_folder) if f.startswith(f"{note}_") and f.endswith('.wav')]
        return max(existing_parts) + 1 if existing_parts else 1
    @classmethod
    def frequency_to_note(cls, frequency):
        A4 = 440
        C0 = A4 * pow(2, -4.75)
        if frequency == 0:
            return "Unknown"
        h = round(12 * math.log2(frequency / C0))
        octave = h // 12
        n = h % 12
        return f"{cls.note_names[n]}{octave}"
    @classmethod
    def note_to_frequency(cls, note):
        A4 = 440
        note_name = ''.join([c for c in note if not c.isdigit()])
        octave = int(''.join([c for c in note if c.isdigit()]))
        semitone = cls.note_names.index(note_name)
        return A4 * pow(2, (octave - 4) + (semitone - 9) / 12)
    @classmethod
    def average_absolute_value(cls, samples):
        return sum(abs(sample) for sample in samples) / len(samples)
    @classmethod
    def convert(cls, audio_data, oscillations, threshold=100, max_threshold=32767, channel=0, phase='full', LowSamplePhaseCount=0, LSPCOperation='ignore'):
        if phase == 'full':
            extracted_oscillations = OscillationExtraction.fullphase(audio_data, channel)
        else:
            extracted_oscillations = OscillationExtraction.singlephase(audio_data, channel, phase, LowSamplePhaseCount, LSPCOperation)
        print(f"Total audio samples: {len(audio_data)}")
        print(f"Total oscillations detected: {len(extracted_oscillations)}")
        for osc in extracted_oscillations:
            if phase == 'full':
                # For full phase, we need to calculate the total count
                total_count = len(osc['samples'])
                samples = osc['samples']
            else:
                total_count = osc['positive_count'] if phase == 'positive' else osc['negative_count']
                samples = osc['samples']
            avg_abs_value = cls.average_absolute_value(samples)
            if threshold <= avg_abs_value <= max_threshold:
                found_match = False
                for note in cls.get_all_notes():
                    expected_count = round(cls.sample_rate / cls.note_to_frequency(note))
                    if phase != 'full':
                        expected_count = expected_count // 2  # Half of the full oscillation for single phase
                    if abs(total_count - expected_count) <= 1:  # Allow for rounding error
                        oscillations[note].extend(samples)
                        print(f"Accepted oscillation for {note}, count: {total_count}")
                        found_match = True
                        break
                if not found_match:
                    print(f"Rejected oscillation, total count: {total_count}")
            elif avg_abs_value > max_threshold:
                print(f"Rejected oscillation due to high average absolute value")
            else:
                print(f"Rejected oscillation due to low average absolute value")
    @classmethod
    def get_all_notes(cls):
        notes = []
        for octave in range(1, 7):  # 1 to 6
            for note in cls.note_names:
                notes.append(f"{note}{octave}")
        return notes
    @classmethod
    def preprocess_files(cls, input_folder):
        # Process each WAV file in the input folder
        for filename in os.listdir(input_folder):
            if filename.lower().endswith('.wav'):
                input_path = os.path.join(input_folder, filename)
                print(f"Preprocessed {filename}")
        print("Preprocessing completed")

#"------------------------------------------------------------------------------------------------------"

    @classmethod
    def ExtractionSynthesis(cls, input_file, output_folder, incomplete_folder=None, threshold=100, max_threshold=32767, normalize=False, phase='full'):
        output_messages = []
        if not os.path.isfile(input_file):
            print(f"Error: {input_file} is not a valid file.")
            output_messages.append(f"Error: {input_file} is not a valid file.\n")
            return output_messages

        if not input_file.lower().endswith('.wav'):
            print(f"Error: {input_file} is not a WAV file.")
            output_messages.append(f"Error: {input_file} is not a WAV file.\n")
            return output_messages

        temp_folder = os.path.join(os.path.dirname(input_file), 'temp')
        if os.path.exists(temp_folder):
            shutil.rmtree(temp_folder)
        os.makedirs(temp_folder)

        def clear_output():
            if sys.platform.startswith('win'):
                os.system('cls')
            else:
                os.system('clear')

        def save_oscillations(note, samples):
            if len(samples) > 0:
                if phase == 'positive':
                    samples = [abs(s) for s in samples]
                elif phase == 'negative':
                    samples = [-abs(s) for s in samples]
                while len(samples) < cls.sample_rate * 10:
                    samples.extend(samples[:min(len(samples), cls.sample_rate * 10 - len(samples))])
                note_folder = os.path.join(output_folder, note)
                os.makedirs(note_folder, exist_ok=True)
                chunks = [samples[i:i + cls.sample_rate * 10] for i in range(0, len(samples), cls.sample_rate * 10)]
                for chunk in chunks:
                    part_number = cls.get_next_part_number(note_folder, note)
                    output_file = os.path.join(note_folder, f"{note}_{part_number}.wav")
                    AudioSampleValues.list_to_mono_wav(chunk, output_file)
                    print(f"Successfully created audio sample for {note} (part {part_number})")
                    output_messages.append(f"Successfully created audio sample for {note} (part {part_number})\n")

        def process_file(file_path):
            print(f"Processing file: {file_path}")
            output_messages.append(f"Processing file: {file_path}\n")
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            processed_path = os.path.join(temp_folder, f"processed_{base_name}.wav")
            info = sf.info(file_path)
            if info.subtype != 'PCM_16' or info.samplerate != 44100 or info.channels != 2:
                print(f"Converting to 16-bit stereo 44100 Hz WAV")
                output_messages.append(f"Converting to 16-bit stereo 44100 Hz WAV\n")
                AudioProselyte.wav_to_wav(file_path, processed_path)
            else:
                print(f"File is already in correct format")
                output_messages.append(f"File is already in correct format\n")
                shutil.copy(file_path, processed_path)

            if normalize:
                print(f"Normalizing audio")
                output_messages.append(f"Normalizing audio\n")
                AudioNormalize.normalize(processed_path, processed_path)

            print(f"Processing {'normalized' if normalize else 'original'} file")
            output_messages.append(f"Processing {'normalized' if normalize else 'original'} file\n")
            process_audio_file(processed_path, "normalized" if normalize else "original")
            clear_output()

        def process_audio_file(file_path, file_type):
            audio_data = AudioSampleValues.wav_to_list(file_path)
            oscillations = {note: [] for note in cls.get_all_notes()}
            print(f"Processing {file_type} - left channel")
            output_messages.append(f"Processing {file_type} - left channel\n")
            cls.convert(audio_data, oscillations, threshold, max_threshold, channel=0, phase=phase)
            for note, samples in oscillations.items():
                save_oscillations(note, samples)

            oscillations = {note: [] for note in cls.get_all_notes()}
            print(f"Processing {file_type} - right channel")
            output_messages.append(f"Processing {file_type} - right channel\n")
            cls.convert(audio_data, oscillations, threshold, max_threshold, channel=1, phase=phase)
            for note, samples in oscillations.items():
                save_oscillations(note, samples)

        process_file(input_file)
        print(f"Finished processing audio file: {input_file}")
        output_messages.append(f"Finished processing audio file: {input_file}\n")
        shutil.rmtree(temp_folder)
        return output_messages


#"------------------------------------------------------------------------------------------------------"

    @classmethod
    def DissectionSynthesis(cls, input_wav_path, output_dir, mode='Octave+', process_type='pitch', combine=False):
        """
        Process audio using either pitch-based or temporal-based dissection synthesis.
        
        Parameters:
        - input_wav_path: Path to the input WAV file
        - output_dir: Directory to save the output WAV file
        - mode: For pitch: 'Octave+' or 'Octave-'; For temporal: 'TDSSlow' or 'TDSFast'
        - process_type: 'pitch' or 'temporal' to determine which algorithm to use
        - combine: Whether to combine processed audio with original (only for pitch type)
        
        Returns:
        - Path to the output WAV file
        """
        try:
            print(f"Starting {process_type} dissection synthesis ({mode}) for input file: {input_wav_path}")
            samples = AudioSampleValues.wav_to_list(input_wav_path)
            print(f"Samples loaded. Shape: {np.array(samples).shape}, Type: {type(samples)}")
            if not samples:
                raise ValueError("No samples were loaded from the input file.")
            
            # Process audio based on type
            if process_type.lower() == 'pitch':
                processed_samples = cls._process_audio_pitch(samples, mode, combine)
            elif process_type.lower() == 'temporal':
                processed_samples = cls._process_audio_temporal(samples, mode)
            else:
                raise ValueError(f"Unknown process_type: {process_type}. Must be 'pitch' or 'temporal'")
            
            print(f"Audio processed. Processed samples shape: {np.array(processed_samples).shape}")
            if not processed_samples:
                raise ValueError("No samples were produced after processing.")
            
            # Generate output filename
            input_filename = os.path.basename(input_wav_path)
            input_name, _ = os.path.splitext(input_filename)
            output_filename = f"{input_name}_{mode}.wav"
            output_wav_path = os.path.join(output_dir, output_filename)
            
            os.makedirs(output_dir, exist_ok=True)
            AudioSampleValues.list_to_wav(processed_samples, output_wav_path)
            print(f"Audio processing completed. Output saved to: {output_wav_path}")
            return output_wav_path
        except Exception as e:
            print(f"An error occurred: {e}")
            import traceback
            traceback.print_exc()

    @classmethod
    def _process_audio_pitch(cls, audio_data, harmonic, combine):
        """Process audio using pitch-based dissection synthesis."""
        print(f"Starting pitch audio processing for {harmonic}...")
        left_channel = [sample[0] for sample in audio_data]
        right_channel = [sample[1] for sample in audio_data]
        
        if harmonic == 'Octave+':
            processed_left = cls._process_channel_octave_plus(left_channel)
            processed_right = cls._process_channel_octave_plus(right_channel)
        elif harmonic == 'Octave-':
            processed_left = cls._process_channel_octave_minus(left_channel)
            processed_right = cls._process_channel_octave_minus(right_channel)
        else:
            raise ValueError(f"Unknown harmonic: {harmonic}")
        
        print(f"Original left channel length: {len(left_channel)}")
        print(f"Processed left channel length: {len(processed_left)}")
        print(f"Original right channel length: {len(right_channel)}")
        print(f"Processed right channel length: {len(processed_right)}")
        
        if combine:
            return cls._combine_and_normalize(audio_data, processed_left, processed_right)
        else:
            return cls._normalize_channels(processed_left, processed_right)

    @classmethod
    def _process_audio_temporal(cls, audio_data, mode):
        """Process audio using temporal-based dissection synthesis."""
        print(f"Starting temporal audio processing for {mode}...")
        left_channel = [sample[0] for sample in audio_data]
        right_channel = [sample[1] for sample in audio_data]
        
        if mode == 'TDSSlow':
            processed_left = cls._process_channel_tds_slow(left_channel)
            processed_right = cls._process_channel_tds_slow(right_channel)
        elif mode == 'TDSFast':
            processed_left, left_indices = cls._process_channel_tds_fast(left_channel)
            processed_right = cls._copy_samples_by_indices(right_channel, left_indices)
        else:
            raise ValueError(f"Unknown mode: {mode}")
        
        print(f"Original left channel length: {len(left_channel)}")
        print(f"Processed left channel length: {len(processed_left)}")
        print(f"Original right channel length: {len(right_channel)}")
        print(f"Processed right channel length: {len(processed_right)}")
        
        return list(zip(processed_left, processed_right))

    # Pitch processing methods
    @classmethod
    def _process_channel_octave_plus(cls, channel_data):
        dissection_harmonics = []
        current_oscillation = []
        state = 'zero'
        zero_count = 0
        
        for value in channel_data:
            if state == 'zero':
                if value > 0:
                    state = 'positive'
                    current_oscillation = [0] * zero_count + [value]
                    zero_count = 0
                elif value < 0:
                    state = 'negative'
                    current_oscillation = [0] * zero_count + [value]
                    zero_count = 0
                else:
                    zero_count += 1
            elif state == 'positive':
                if value >= 0:
                    current_oscillation.append(value)
                else:
                    state = 'negative'
                    current_oscillation.append(value)
            else:  # state == 'negative'
                if value <= 0:
                    current_oscillation.append(value)
                else:
                    # Process completed oscillation
                    processed_oscillation = cls._process_oscillation_octave_plus(current_oscillation)
                    dissection_harmonics.extend(processed_oscillation)
                    # Start new oscillation
                    state = 'positive'
                    current_oscillation = [value]
        
        # Process any remaining oscillation
        if current_oscillation:
            processed_oscillation = cls._process_oscillation_octave_plus(current_oscillation)
            dissection_harmonics.extend(processed_oscillation)
        
        # Add any remaining zeros
        dissection_harmonics.extend([0] * zero_count)
        
        assert len(dissection_harmonics) == len(channel_data), f"Processed channel length ({len(dissection_harmonics)}) does not match original ({len(channel_data)})"
        return dissection_harmonics

    @classmethod
    def _process_oscillation_octave_plus(cls, oscillation):
        oscillation_length = len(oscillation)
        if oscillation_length <= 2:
            return oscillation
        
        reduced_oscillation = oscillation[::2]
        processed_oscillation = reduced_oscillation * 2
        return processed_oscillation[:oscillation_length]

    @classmethod
    def _process_channel_octave_minus(cls, channel_data):
        dissection_harmonics = []
        current_oscillation = []
        state = 'zero'
        zero_count = 0
        
        for value in channel_data:
            if state == 'zero':
                if value > 0:
                    state = 'positive'
                    current_oscillation = [0] * zero_count + [value]
                    zero_count = 0
                elif value < 0:
                    state = 'negative'
                    current_oscillation = [0] * zero_count + [value]
                    zero_count = 0
                else:
                    zero_count += 1
            elif state == 'positive':
                if value >= 0:
                    current_oscillation.append(value)
                else:
                    state = 'negative'
                    current_oscillation.append(value)
            else:  # state == 'negative'
                if value <= 0:
                    current_oscillation.append(value)
                else:
                    # Process completed oscillation
                    processed_oscillation = cls._process_oscillation_octave_minus(current_oscillation)
                    dissection_harmonics.extend(processed_oscillation)
                    # Start new oscillation
                    state = 'positive'
                    current_oscillation = [value]
        
        # Process any remaining oscillation
        if current_oscillation:
            processed_oscillation = cls._process_oscillation_octave_minus(current_oscillation)
            dissection_harmonics.extend(processed_oscillation)
        
        # Add any remaining zeros
        dissection_harmonics.extend([0] * zero_count)
        
        assert len(dissection_harmonics) == len(channel_data), f"Processed channel length ({len(dissection_harmonics)}) does not match original ({len(channel_data)})"
        return dissection_harmonics

    @classmethod
    def _process_oscillation_octave_minus(cls, oscillation):
        oscillation_length = len(oscillation)
        if oscillation_length <= 2:
            return oscillation
        
        # Double the oscillation by adding interpolated values
        doubled_oscillation = []
        for i in range(len(oscillation) - 1):
            doubled_oscillation.append(oscillation[i])
            doubled_oscillation.append((oscillation[i] + oscillation[i+1]) / 2)
        doubled_oscillation.append(oscillation[-1])
        
        # Cut the doubled oscillation in half
        processed_oscillation = doubled_oscillation[:oscillation_length]
        return processed_oscillation

    # Temporal processing methods
    @classmethod
    def _process_channel_tds_slow(cls, channel_data):
        processed_data = []
        current_oscillation = []
        state = 'zero'
        
        for value in channel_data:
            if state == 'zero':
                if value > 0:
                    state = 'positive'
                    current_oscillation = [value]
                elif value < 0:
                    state = 'negative'
                    current_oscillation = [value]
                else:
                    processed_data.append(value)
            elif state == 'positive':
                if value >= 0:
                    current_oscillation.append(value)
                else:
                    state = 'negative'
                    current_oscillation.append(value)
            else:  # state == 'negative'
                if value <= 0:
                    current_oscillation.append(value)
                else:
                    # Process completed oscillation
                    processed_data.extend(current_oscillation)
                    processed_data.extend(current_oscillation)  # Duplicate the oscillation
                    # Start new oscillation
                    state = 'positive'
                    current_oscillation = [value]
        
        # Process any remaining oscillation
        if current_oscillation:
            processed_data.extend(current_oscillation)
            processed_data.extend(current_oscillation)
        
        return processed_data

    @classmethod
    def _process_channel_tds_fast(cls, channel_data):
        processed_data = []
        current_oscillation = []
        state = 'zero'
        include_oscillation = True
        indices = []
        current_index = 0
        
        for value in channel_data:
            if state == 'zero':
                if value > 0:
                    state = 'positive'
                    current_oscillation = [value]
                elif value < 0:
                    state = 'negative'
                    current_oscillation = [value]
                else:
                    if include_oscillation:
                        processed_data.append(value)
                        indices.append(current_index)
            elif state == 'positive':
                if value >= 0:
                    current_oscillation.append(value)
                else:
                    state = 'negative'
                    current_oscillation.append(value)
            else:  # state == 'negative'
                if value <= 0:
                    current_oscillation.append(value)
                else:
                    # Process completed oscillation
                    if include_oscillation:
                        processed_data.extend(current_oscillation)
                        indices.extend(range(current_index - len(current_oscillation), current_index))
                    include_oscillation = not include_oscillation
                    # Start new oscillation
                    state = 'positive'
                    current_oscillation = [value]
            
            current_index += 1
        
        # Process any remaining oscillation
        if current_oscillation and include_oscillation:
            processed_data.extend(current_oscillation)
            indices.extend(range(current_index - len(current_oscillation), current_index))
        
        return processed_data, indices

    @classmethod
    def _copy_samples_by_indices(cls, channel_data, indices):
        return [channel_data[i] for i in indices]

    # Utility methods
    @classmethod
    def _combine_and_normalize(cls, original_data, processed_left, processed_right):
        combined_samples = []
        for i in range(len(original_data)):
            left_combined = original_data[i][0] + processed_left[i]
            right_combined = original_data[i][1] + processed_right[i]
            combined_samples.append([left_combined, right_combined])
        
        return cls._normalize_channels(combined_samples)

    @classmethod
    def _normalize_channels(cls, left_channel, right_channel=None):
        if right_channel is None:
            # If only one channel is provided, assume it's a list of [left, right] pairs
            channels = list(zip(*left_channel))
            left_channel, right_channel = channels[0], channels[1]
        
        max_value = max(max(abs(x) for x in left_channel), max(abs(x) for x in right_channel))
        if max_value > 32767:
            scale_factor = 32767 / max_value
            left_channel = [int(x * scale_factor) for x in left_channel]
            right_channel = [int(x * scale_factor) for x in right_channel]
        
        return list(zip(left_channel, right_channel))


#IncisionSynthesis is currently unfinished
#"------------------------------------------------------------------------------------------------------"

    @classmethod
    def IncisionSynthesis(cls, input_wav_path, output_dir, waveform='sine', amplitude=1, LowSamplePhaseCount=0, LSPCOperation='ignore'):
        try:
            print(f"Starting processing for input file: {input_wav_path}")
            samples = AudioSampleValues.wav_to_list(input_wav_path)
            print(f"Samples loaded. Shape: {np.array(samples).shape}, Type: {type(samples)}")
            if not samples:
                raise ValueError("No samples were loaded from the input file.")
            
            processed_samples = cls.process_audio_with_waveform(samples, waveform, amplitude, LowSamplePhaseCount, LSPCOperation)
            print(f"Audio processed. Processed samples shape: {np.array(processed_samples).shape}")
            if not processed_samples:
                raise ValueError("No samples were produced after processing.")
            
            # Generate output filename
            input_filename = os.path.basename(input_wav_path)
            input_name, _ = os.path.splitext(input_filename)
            output_filename = f"{input_name}_{waveform}_incision.wav"
            output_wav_path = os.path.join(output_dir, output_filename)
            
            os.makedirs(output_dir, exist_ok=True)
            AudioSampleValues.list_to_wav(processed_samples, output_wav_path)
            print(f"Audio processing completed. Output saved to: {output_wav_path}")
            return output_wav_path
        except Exception as e:
            print(f"An error occurred: {e}")
            import traceback
            traceback.print_exc()

    @classmethod
    def process_audio_with_waveform(cls, audio_data, waveform, amplitude, LowSamplePhaseCount, LSPCOperation):
        print(f"Starting audio processing with {waveform} waveform...")
        
        # Process left channel
        left_oscillations = OscillationExtraction.fullphase(audio_data, channel=0, LowSamplePhaseCount=LowSamplePhaseCount, LSPCOperation=LSPCOperation)
        
        # Process right channel
        right_oscillations = OscillationExtraction.fullphase(audio_data, channel=1, LowSamplePhaseCount=LowSamplePhaseCount, LSPCOperation=LSPCOperation)
        
        processed_samples = []
        for left_osc, right_osc in zip(left_oscillations, right_oscillations):
            left_processed = cls.process_oscillation(left_osc['samples'], waveform, amplitude)
            right_processed = cls.process_oscillation(right_osc['samples'], waveform, amplitude)
            
            # Combine left and right channels
            processed_samples.extend(list(zip(left_processed, right_processed)))
        
        # Ensure the processed samples have the same length as the original
        if len(processed_samples) > len(audio_data):
            print(f"Truncating processed samples from {len(processed_samples)} to {len(audio_data)}")
            processed_samples = processed_samples[:len(audio_data)]
        elif len(processed_samples) < len(audio_data):
            print(f"Padding processed samples from {len(processed_samples)} to {len(audio_data)}")
            processed_samples.extend([(0, 0)] * (len(audio_data) - len(processed_samples)))
        
        assert len(processed_samples) == len(audio_data), f"Processed samples length ({len(processed_samples)}) does not match original ({len(audio_data)})"
        
        return cls.normalize_samples(processed_samples)

    @classmethod
    def process_oscillation(cls, oscillation, waveform, amplitude):
        oscillation_length = len(oscillation)
        if oscillation_length <= 2:
            return oscillation
        
        # Calculate average absolute value of the oscillation
        avg_abs_value = sum(abs(sample) for sample in oscillation) / oscillation_length
        
        # Scale the amplitude based on the average absolute value
        scaled_amplitude = amplitude * (avg_abs_value / 32767)  # Normalize to 16-bit range
        
        # Generate waveform
        waveform_function = getattr(Waveforms, waveform)
        added_waveform = waveform_function(oscillation_length, scaled_amplitude)
        
        # Add waveform to original oscillation
        processed_oscillation = [
            o + w for o, w in zip(oscillation, added_waveform)
        ]
        
        return processed_oscillation

    @classmethod
    def normalize_samples(cls, samples):
        left_channel = [sample[0] for sample in samples]
        right_channel = [sample[1] for sample in samples]
        
        max_value = max(max(abs(x) for x in left_channel), max(abs(x) for x in right_channel))
        if max_value > 32767:
            scale_factor = 32767 / max_value
            left_channel = [int(x * scale_factor) for x in left_channel]
            right_channel = [int(x * scale_factor) for x in right_channel]
        
        return list(zip(left_channel, right_channel))


#SurgicalSynthesis.DissectionSynthesis("C:/Audio/Embryo.wav", "C:/Audio/Embryo", mode='TDSFast', process_type='temporal', combine=False)