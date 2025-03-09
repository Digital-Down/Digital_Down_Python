import numpy as np
import os
from .AudioSampleValues import *
from .Waveforms import Waveforms
from .OscillationExtraction import OscillationExtraction

class IncisionSynthesis:
    @classmethod
    def process_audio(cls, input_wav_path, output_dir, waveform='sine', amplitude=1, LowSamplePhaseCount=0, LSPCOperation='ignore'):
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

# Example usage
#if __name__ == "__main__":
#    input_wav_path = "C:/Audio/Vocals.wav"
#    output_dir = "D:/Audio"
#    IncisionSynthesis.process_audio(input_wav_path, output_dir, waveform='square', amplitude=0.3, LowSamplePhaseCount=0, LSPCOperation='ignore')