"""
__________________________________________________________________________________
#####################
##AudioSampleValues##
#####################
__________________________________________________________________________________

###########
##Methods##
###########

1.wav_to_list		converts a wav to a stereo list of raw audio values
2.list_to_wav		converts a list of raw audio values to wav
__________________________________________________________________________________
####################
##Method Arguments##
####################
User Defined Arguments
1. wav_to_list			WAV File Name.wav
2. list_to_wav			[List]


# Convert the WAV to a list and then back to a WAV file
AudioSampleValues.list_to_wav([AudioSampleValues.wav_to_list('Words.wav')])
__________________________________________________________________________________
"""
import numpy as np
import wave
import os
######
#Main#
######

class AudioSampleValues:
    @classmethod
    def wav_to_list(cls, wav_file_path):
        if not os.path.exists(wav_file_path):
            raise FileNotFoundError(f"The file {wav_file_path} does not exist.")
        try:
            with wave.open(wav_file_path, 'rb') as wav:
                frames = wav.readframes(wav.getnframes())
                samples = np.frombuffer(frames, dtype=np.int16)
                samples = samples.reshape(-1, wav.getnchannels())
            return samples.tolist()
        except Exception as e:
            raise IOError(f"Error reading WAV file {wav_file_path}: {str(e)}")

    @classmethod
    def list_to_wav(cls, samples_list, output_file):
        try:
            samples_array = np.array(samples_list, dtype=np.int16)
            
            # Ensure the samples are in the correct shape (n_samples, n_channels)
            if samples_array.ndim == 1:
                samples_array = samples_array.reshape(-1, 1)  # Mono
            elif samples_array.ndim > 2:
                raise ValueError("Invalid sample array shape. Expected 1D or 2D array.")

            n_channels = samples_array.shape[1]
            
            with wave.open(output_file, 'wb') as wav_file:
                wav_file.setnchannels(n_channels)
                wav_file.setsampwidth(2)  # 16-bit audio
                wav_file.setframerate(44100)  # Assuming 44.1kHz sample rate
                wav_file.writeframes(samples_array.tobytes())
            
            print(f"Successfully wrote WAV file to {output_file}")
        except Exception as e:
            raise IOError(f"Error writing WAV file {output_file}: {str(e)}")

    @classmethod
    def list_to_mono_wav(cls, samples_list, output_file):
        try:
            samples_array = np.array(samples_list, dtype=np.int16)
            
            # Ensure the samples are in the correct shape for mono (n_samples,)
            if samples_array.ndim == 2:
                samples_array = samples_array.mean(axis=1).astype(np.int16)
            elif samples_array.ndim > 2:
                raise ValueError("Invalid sample array shape. Expected 1D or 2D array.")

            with wave.open(output_file, 'wb') as wav_file:
                wav_file.setnchannels(1)  # Mono
                wav_file.setsampwidth(2)  # 16-bit audio
                wav_file.setframerate(44100)  # Assuming 44.1kHz sample rate
                wav_file.writeframes(samples_array.tobytes())
            
            print(f"Successfully wrote mono WAV file to {output_file}")
        except Exception as e:
            raise IOError(f"Error writing mono WAV file {output_file}: {str(e)}")

    @classmethod
    def wavs_to_list(cls, folder_path):
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder {folder_path} does not exist.")
        all_samples = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.wav'):
                file_path = os.path.join(folder_path, file_path)
                samples = cls.wav_to_list(file_path)
                all_samples.extend(samples)
        return all_samples