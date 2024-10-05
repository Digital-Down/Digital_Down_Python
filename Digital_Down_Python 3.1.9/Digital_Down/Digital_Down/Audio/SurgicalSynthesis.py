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
from .OscillationExtraction import *
from .AudioNormalize import *
from .AudioProselyte import *
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
    def convert(cls, audio_data, oscillations, threshold=100, max_threshold=32767, channel=0, phase='full', LowSamplePhaseCount=3, LSPCOperation='omit'):
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
    @classmethod
    def DissectionSynthesis():
        pass

    @classmethod
    def IncisionSynthesis():
        pass