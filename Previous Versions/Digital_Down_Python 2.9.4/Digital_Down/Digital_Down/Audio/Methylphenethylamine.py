import os
from .AudioSampleValues import *

class Methylphenethylamine:
    @classmethod
    def slow(cls, audio_file_path, iterations):
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"The file {audio_file_path} does not exist.")
        
        samples_list = AudioSampleValues.wav_to_list(audio_file_path)
        samples = samples_list[0]
        
        def interpolate(a, b):
            return [round((a[0] + b[0]) / 2), round((a[1] + b[1]) / 2)]
        
        for _ in range(iterations):
            new_samples = []
            for i in range(len(samples) - 1):
                new_samples.append(samples[i])
                new_samples.append(interpolate(samples[i], samples[i + 1]))
            new_samples.append(samples[-1])
            samples = new_samples
        return [samples]

    @classmethod
    def fast(cls, audio_file_path, iterations):
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"The file {audio_file_path} does not exist.")
        samples_list = AudioSampleValues.wav_to_list(audio_file_path)
        samples = samples_list[0]
        for _ in range(iterations):
            samples = [samples[i] for i in range(len(samples)) if i % 2 == 0]
        return [samples]
#Fast acceptable range is 1-6
#Slow acceptable range is 1