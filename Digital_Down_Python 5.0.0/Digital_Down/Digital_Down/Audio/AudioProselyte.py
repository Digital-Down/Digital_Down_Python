import numpy as np
from pydub import AudioSegment

class AudioProselyte:
    @classmethod
    def wav_to_wav(cls, input_file, output_file, SR=44100, Stereo=True, BD=16):
        # Load the audio file
        audio = AudioSegment.from_file(input_file)
        
        # Convert to stereo if Stereo is True and the audio is mono
        if Stereo and audio.channels == 1:
            audio = audio.set_channels(2)
        # Convert to mono if Stereo is False and the audio is stereo
        elif not Stereo and audio.channels == 2:
            audio = audio.set_channels(1)
        
        # Set sample rate to SR
        audio = audio.set_frame_rate(SR)
        
        # Set bit depth (sample width)
        sample_width = BD // 8  # Convert bit depth to bytes
        audio = audio.set_sample_width(sample_width)
        
        # Export as WAV
        audio.export(output_file, format="wav")