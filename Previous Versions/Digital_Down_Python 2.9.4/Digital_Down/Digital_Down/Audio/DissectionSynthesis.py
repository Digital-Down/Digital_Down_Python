import numpy as np
import os
from .AudioSampleValues import *

class DissectionSynthesis:
    @classmethod
    def process_audio_with_harmonic(cls, input_wav_path, output_dir, harmonic, combine=True):
        try:
            print(f"Starting {harmonic} processing for input file: {input_wav_path}")
            samples = AudioSampleValues.wav_to_list(input_wav_path)
            print(f"Samples loaded. Shape: {np.array(samples).shape}, Type: {type(samples)}")
            if not samples:
                raise ValueError("No samples were loaded from the input file.")
            
            processed_samples = cls.process_audio(samples, harmonic, combine)
            print(f"Audio processed. Processed samples shape: {np.array(processed_samples).shape}")
            if not processed_samples:
                raise ValueError("No samples were produced after processing.")
            
            # Generate output filename
            input_filename = os.path.basename(input_wav_path)
            input_name, _ = os.path.splitext(input_filename)
            output_filename = f"{input_name} {harmonic}.wav"
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
    def process_audio(cls, audio_data, harmonic, combine):
        print(f"Starting audio processing for {harmonic}...")
        left_channel = [sample[0] for sample in audio_data]
        right_channel = [sample[1] for sample in audio_data]
        
        if harmonic == 'Octave+':
            processed_left = cls.process_channel_octave_plus(left_channel)
            processed_right = cls.process_channel_octave_plus(right_channel)
        elif harmonic == 'Octave-':
            processed_left = cls.process_channel_octave_minus(left_channel)
            processed_right = cls.process_channel_octave_minus(right_channel)
        else:
            raise ValueError(f"Unknown harmonic: {harmonic}")
        
        print(f"Original left channel length: {len(left_channel)}")
        print(f"Processed left channel length: {len(processed_left)}")
        print(f"Original right channel length: {len(right_channel)}")
        print(f"Processed right channel length: {len(processed_right)}")
        
        if combine:
            return cls.combine_and_normalize(audio_data, processed_left, processed_right)
        else:
            return cls.normalize_channels(processed_left, processed_right)

    @classmethod
    def process_channel_octave_plus(cls, channel_data):
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
                    processed_oscillation = cls.process_oscillation_octave_plus(current_oscillation)
                    dissection_harmonics.extend(processed_oscillation)
                    # Start new oscillation
                    state = 'positive'
                    current_oscillation = [value]
        
        # Process any remaining oscillation
        if current_oscillation:
            processed_oscillation = cls.process_oscillation_octave_plus(current_oscillation)
            dissection_harmonics.extend(processed_oscillation)
        
        # Add any remaining zeros
        dissection_harmonics.extend([0] * zero_count)
        
        assert len(dissection_harmonics) == len(channel_data), f"Processed channel length ({len(dissection_harmonics)}) does not match original ({len(channel_data)})"
        return dissection_harmonics

    @classmethod
    def process_oscillation_octave_plus(cls, oscillation):
        oscillation_length = len(oscillation)
        if oscillation_length <= 2:
            return oscillation
        
        reduced_oscillation = oscillation[::2]
        processed_oscillation = reduced_oscillation * 2
        return processed_oscillation[:oscillation_length]

    @classmethod
    def process_channel_octave_minus(cls, channel_data):
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
                    processed_oscillation = cls.process_oscillation_octave_minus(current_oscillation)
                    dissection_harmonics.extend(processed_oscillation)
                    # Start new oscillation
                    state = 'positive'
                    current_oscillation = [value]
        
        # Process any remaining oscillation
        if current_oscillation:
            processed_oscillation = cls.process_oscillation_octave_minus(current_oscillation)
            dissection_harmonics.extend(processed_oscillation)
        
        # Add any remaining zeros
        dissection_harmonics.extend([0] * zero_count)
        
        assert len(dissection_harmonics) == len(channel_data), f"Processed channel length ({len(dissection_harmonics)}) does not match original ({len(channel_data)})"
        return dissection_harmonics

    @classmethod
    def process_oscillation_octave_minus(cls, oscillation):
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

    @classmethod
    def combine_and_normalize(cls, original_data, processed_left, processed_right):
        combined_samples = []
        for i in range(len(original_data)):
            left_combined = original_data[i][0] + processed_left[i]
            right_combined = original_data[i][1] + processed_right[i]
            combined_samples.append([left_combined, right_combined])
        
        return cls.normalize_channels(combined_samples)

    @classmethod
    def normalize_channels(cls, left_channel, right_channel=None):
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

    # Individual harmonic methods
    @classmethod
    def OctavePlus(cls, input_wav_path, output_dir, combine=False):
        return cls.process_audio_with_harmonic(input_wav_path, output_dir, 'Octave+', combine)

    @classmethod
    def OctaveMinus(cls, input_wav_path, output_dir, combine=False):
        return cls.process_audio_with_harmonic(input_wav_path, output_dir, 'Octave-', combine)
