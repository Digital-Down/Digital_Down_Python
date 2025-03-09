import numpy as np
import os
from .AudioSampleValues import *

class TemporalDissectionSynthesis:
    @classmethod
    def process_audio_with_temporal(cls, input_wav_path, output_dir, mode):
        try:
            print(f"Starting {mode} processing for input file: {input_wav_path}")
            samples = AudioSampleValues.wav_to_list(input_wav_path)
            print(f"Samples loaded. Shape: {np.array(samples).shape}, Type: {type(samples)}")
            if not samples:
                raise ValueError("No samples were loaded from the input file.")
            
            processed_samples = cls.process_audio(samples, mode)
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
    def process_audio(cls, audio_data, mode):
        print(f"Starting audio processing for {mode}...")
        left_channel = [sample[0] for sample in audio_data]
        right_channel = [sample[1] for sample in audio_data]
        
        if mode == 'TDSSlow':
            processed_left = cls.process_channel_tds_slow(left_channel)
            processed_right = cls.process_channel_tds_slow(right_channel)
        elif mode == 'TDSFast':
            processed_left, left_indices = cls.process_channel_tds_fast(left_channel)
            processed_right = cls.copy_samples_by_indices(right_channel, left_indices)
        else:
            raise ValueError(f"Unknown mode: {mode}")
        
        print(f"Original left channel length: {len(left_channel)}")
        print(f"Processed left channel length: {len(processed_left)}")
        print(f"Original right channel length: {len(right_channel)}")
        print(f"Processed right channel length: {len(processed_right)}")
        
        return list(zip(processed_left, processed_right))

    @classmethod
    def process_channel_tds_slow(cls, channel_data):
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
    def process_channel_tds_fast(cls, channel_data):
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
    def copy_samples_by_indices(cls, channel_data, indices):
        return [channel_data[i] for i in indices]

    # Individual temporal methods
    @classmethod
    def TDSSlow(cls, input_wav_path, output_dir):
        return cls.process_audio_with_temporal(input_wav_path, output_dir, 'TDSSlow')

    @classmethod
    def TDSFast(cls, input_wav_path, output_dir):
        return cls.process_audio_with_temporal(input_wav_path, output_dir, 'TDSFast')
