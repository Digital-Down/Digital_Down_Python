import numpy as np
import soundfile as sf
import os

class AudioNormalize:
    @classmethod
    def normalize(cls, input_file, output_file, max_value=None):
        audio_data, sample_rate = sf.read(input_file)
        audio_data = audio_data.astype(np.float64)
        
        if max_value is None:
            max_value = np.max(np.abs(audio_data))
        
        if max_value > 0:
            normalized_audio = audio_data / max_value
        else:
            normalized_audio = audio_data
        
        sf.write(output_file, normalized_audio, sample_rate, subtype='PCM_16')
        
        return max_value

    @classmethod
    def batchnormalize(cls, input_folder, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # First pass: find the maximum value across all files
        max_value = 0
        for filename in os.listdir(input_folder):
            if filename.endswith(('.wav', '.flac')):  # Add more audio formats if needed
                input_file = os.path.join(input_folder, filename)
                audio_data, _ = sf.read(input_file)
                file_max = np.max(np.abs(audio_data))
                max_value = max(max_value, file_max)
        
        # Second pass: normalize all files using the found max_value
        for filename in os.listdir(input_folder):
            if filename.endswith(('.wav', '.flac')):
                input_file = os.path.join(input_folder, filename)
                output_file = os.path.join(output_folder, filename)
                cls.normalize(input_file, output_file, max_value)
        
        print(f"Batch normalization complete for folder {input_folder}. Max value used: {max_value}")

    @classmethod
    def multiplebatchnormalize(cls, input_root, output_root):
        def process_folder(input_folder, output_folder):
            # Create the output folder if it doesn't exist
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            # Process audio files in the current folder
            cls.batchnormalize(input_folder, output_folder)
            
            # Recursively process subfolders
            for item in os.listdir(input_folder):
                input_path = os.path.join(input_folder, item)
                output_path = os.path.join(output_folder, item)
                if os.path.isdir(input_path):
                    process_folder(input_path, output_path)
        
        # Start processing from the root folders
        process_folder(input_root, output_root)
        print(f"Multiple batch normalization complete. Processed folder structure: {input_root}")