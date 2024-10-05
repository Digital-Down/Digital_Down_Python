import numpy as np
import soundfile as sf

class AudioNormalize:
    @classmethod
    def normalize(cls, input_file, output_file):
        audio_data, sample_rate = sf.read(input_file)
        audio_data = audio_data.astype(np.float64)
        max_value = np.max(np.abs(audio_data))
        if max_value > 0:
            normalized_audio = audio_data / max_value
        else:
            normalized_audio = audio_data
        sf.write(output_file, normalized_audio, sample_rate, subtype='PCM_16')

    @classmethod
    def batchnormalize(cls, inputfolder, outputfolder):
        pass