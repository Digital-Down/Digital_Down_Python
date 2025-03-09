import os
import numpy as np
import operator
from .AudioSampleValues import *
from .NonLinearWaveforms import *
from .NonLinearAudio import *
from .Waveforms import *

class OperationalSynthesis:
    SAMPLE_RATE = 44100  # Standard sample rate
    @staticmethod
    def _scale_to_bit_range(samples, bits):
        """Scale samples to a floating point range based on the number of bits."""
        max_value = 2**(bits - 1)
        return np.array(samples, dtype=float) / 32768 * max_value

    @classmethod
    def _generate_waveform(cls, wave_func, length, amplitude, target_length, nonlinear=True, nonlinearity=100, temporal_chance=50, stereo=False):
        """Generate a waveform and repeat it to match the target length."""
        samples = []
        while len(samples) < target_length:
            if stereo:
                if nonlinear:
                    left_samples = getattr(NonLinearWaveforms, wave_func)(length, amplitude, nonlinearity, temporal_chance)
                    right_samples = getattr(NonLinearWaveforms, wave_func)(length, amplitude, nonlinearity, temporal_chance)
                else:
                    left_samples = getattr(Waveforms, wave_func)(length, amplitude)
                    right_samples = getattr(Waveforms, wave_func)(length, amplitude)
                new_samples = list(zip(left_samples, right_samples))
            else:
                if nonlinear:
                    new_samples = getattr(NonLinearWaveforms, wave_func)(length, amplitude, nonlinearity, temporal_chance)
                else:
                    new_samples = getattr(Waveforms, wave_func)(length, amplitude)
            samples.extend(new_samples)
        return samples[:target_length]

    @classmethod
    def _waveform_operation(cls, wave1_func, wave1_length, wave1_amplitude, 
                           wave2_func, wave2_length, wave2_amplitude, 
                           operation, output_file, divisive_power=1, time=1, 
                           nonlinear=True, stereo=False, DVAbsolute=False):
        target_length = int(cls.SAMPLE_RATE * time)
        wave1_samples = cls._generate_waveform(wave1_func, wave1_length, wave1_amplitude, target_length, nonlinear, stereo=stereo)
        wave2_samples = cls._generate_waveform(wave2_func, wave2_length, wave2_amplitude, target_length, nonlinear, stereo=stereo)
    
        processed_samples = cls._apply_operation(wave1_samples, wave2_samples, operation, divisive_power, stereo, DVAbsolute)
        normalized_samples = cls._normalize(processed_samples)
        AudioSampleValues.list_to_wav(normalized_samples, output_file)

    @staticmethod
    def _apply_operation(input_samples, waveform_samples, operation, divisive_power=1, stereo=False, DVAbsolute=False):
        result = []
        op_func = getattr(operator, operation)
    
        if operation == 'truediv':
            if DVAbsolute:
                if stereo:
                    waveform_samples = [
                        [np.abs(channel) for channel in sample]
                        for sample in waveform_samples
                    ]
                else:
                    waveform_samples = np.abs(waveform_samples)
                
            if stereo:
                waveform_samples = [
                    [np.round(OperationalSynthesis._scale_to_bit_range(channel, divisive_power)).astype(int) 
                     for channel in sample]
                    for sample in waveform_samples
                ]
            else:
                waveform_samples = np.round(OperationalSynthesis._scale_to_bit_range(waveform_samples, divisive_power)).astype(int)

        for i in range(len(input_samples)):
            waveform_index = i % len(waveform_samples)
            if stereo:
                left_result = OperationalSynthesis._apply_single_operation(input_samples[i][0], waveform_samples[waveform_index][0], op_func, operation)
                right_result = OperationalSynthesis._apply_single_operation(input_samples[i][1], waveform_samples[waveform_index][1], op_func, operation)
                result.append([left_result, right_result])
            else:
                result.append(OperationalSynthesis._apply_single_operation(input_samples[i], waveform_samples[waveform_index], op_func, operation))
    
        return result



    @staticmethod
    def _apply_single_operation(input_value, waveform_value, op_func, operation):
        if operation == 'truediv':
            if waveform_value == 0:
                return input_value
            else:
                return round(op_func(input_value, waveform_value))
        else:
            return op_func(input_value, waveform_value)

    @staticmethod
    def _normalize(samples, bit_depth=16):
        """Normalize the samples to fit within the specified bit depth range."""
        max_value = 2**(bit_depth - 1) - 1
        min_value = -2**(bit_depth - 1)
        
        samples_array = np.array(samples)
        
        if samples_array.ndim == 2:  # Stereo
            max_abs_value = np.max(np.abs(samples_array))
            if max_abs_value > max_value:
                scale_factor = max_value / max_abs_value
                samples_array = samples_array * scale_factor
            
            samples_array = np.clip(samples_array, min_value, max_value)
            return samples_array.astype(np.int16).tolist()
        else:  # Mono
            max_abs_value = np.max(np.abs(samples_array))
            if max_abs_value > max_value:
                scale_factor = max_value / max_abs_value
                samples_array = samples_array * scale_factor
            
            samples_array = np.clip(samples_array, min_value, max_value)
            return samples_array.astype(np.int16).tolist()

    @classmethod
    def Null(cls, wave_func, wave_length, wave_amplitude, output_file, time=1, nonlinear=True, stereo=False):
        """Generate and export a single waveform without any operation."""
        target_length = int(cls.SAMPLE_RATE * time)
        samples = cls._generate_waveform(wave_func, wave_length, wave_amplitude, target_length, nonlinear, stereo=stereo)
        normalized_samples = cls._normalize(samples)
        AudioSampleValues.list_to_wav(normalized_samples, output_file)

    @classmethod
    def Additive(cls, wave1_func, wave1_length, wave1_amplitude, 
                 wave2_func, wave2_length, wave2_amplitude, output_file, time=1, nonlinear=True, stereo=False):
        cls._waveform_operation(wave1_func, wave1_length, wave1_amplitude, 
                                wave2_func, wave2_length, wave2_amplitude, 
                                'add', output_file, time=time, nonlinear=nonlinear, stereo=stereo)

    @classmethod
    def Subtractive(cls, wave1_func, wave1_length, wave1_amplitude, 
                    wave2_func, wave2_length, wave2_amplitude, output_file, time=1, nonlinear=True, stereo=False):
        cls._waveform_operation(wave1_func, wave1_length, wave1_amplitude, 
                                wave2_func, wave2_length, wave2_amplitude, 
                                'sub', output_file, time=time, nonlinear=nonlinear, stereo=stereo)

    @classmethod
    def Multiplicative(cls, wave1_func, wave1_length, wave1_amplitude, 
                       wave2_func, wave2_length, wave2_amplitude, output_file, time=1, nonlinear=True, stereo=False):
        cls._waveform_operation(wave1_func, wave1_length, wave1_amplitude, 
                                wave2_func, wave2_length, wave2_amplitude, 
                                'mul', output_file, time=time, nonlinear=nonlinear, stereo=stereo)

    @classmethod
    def Divisive(cls, wave1_func, wave1_length, wave1_amplitude, 
                 wave2_func, wave2_length, wave2_amplitude, output_file, 
                 divisive_power=1, time=1, nonlinear=True, stereo=False, DVAbsolute=False):
        cls._waveform_operation(wave1_func, wave1_length, wave1_amplitude, 
                              wave2_func, wave2_length, wave2_amplitude, 
                              'truediv', output_file, divisive_power, time=time, 
                              nonlinear=nonlinear, stereo=stereo, DVAbsolute=DVAbsolute)

    @classmethod
    def InputMultiplicative(cls, input_file, waveform_func, length, amplitude=1, output_file=None):
        cls._input_operation(input_file, waveform_func, length, amplitude, 'mul', output_file)

    #Adding a waveform to complex audio input is silly, unless the waveform has repeated oscillations.
    #@classmethod
    #def InputAdditive(cls, input_file, waveform_func, length, amplitude=1, output_file=None):
        #cls._input_operation(input_file, waveform_func, length, amplitude, 'add', output_file)

    #Subtracting a waveform to complex audio input is silly, unless the waveform has repeated oscillations.
    #@classmethod
    #def InputSubtractive(cls, input_file, waveform_func, length, amplitude=1, output_file=None):
        #cls._input_operation(input_file, waveform_func, length, amplitude, 'sub', output_file)
    
    #InputDivisive's input data is too complex to create a meaningful output.
    #@classmethod
    #def InputDivisive(cls, input_file, waveform_func, length, amplitude=1, output_file=None, divisive_power=1):
        #cls._input_operation(input_file, waveform_func, length, amplitude, 'truediv', output_file, divisive_power)

# Example usage
#Acceptable Ranges
#Divise Power 2-8
#Octave1-Octave4

'''SampleCountIndexWaveform1 = [C1:1348, 1273, 1201, 1134, 1070, 1010, 953, 900, 849, 802, 757, 714,
    674, 636, 601, 567, 535, 505, 477, 450, 425, 401, 378, 357,
    337, 318, 300, 283, 268, 253, 238, 225, 212, 200, 189, 179,
    169, 159, 150, 142, 134, 126, 119, 113, 106, 100, 95, 89]

SampleCountIndexWaveform1 = [
    1348, 1273, 1201, 1134, 1070, 1010, 953, 900, 849, 802, 757, 714,
    674, 636, 601, 567, 535, 505, 477, 450, 425, 401, 378, 357,
    337, 318, 300, 283, 268, 253, 238, 225, 212, 200, 189, 179,
    169, 159, 150, 142, 134, 126, 119, 113, 106, 100, 95, 89,
    84, 80, 75, 71, 67, 63, 60, 56, 53, 50, 47, 45,
    42, 40, 38, 35, 33, 32, 30, 28, 27, 25, 24, 22
]

DivisivePowerIndex = [2,3,4,5,6,7,8]

OperationalSynthesis.Divisive('sine', 674, 0.5, 'sine', 22, 0.5, 'D:/Audio/DivisiveSynthesisWaveforms/DivisivePower2/SineO0S0SineO0S0/C1.wav', divisive_power=8, time=10, nonlinear=True, stereo=False)'''

import os
from itertools import product

def batch_divisive_synthesis_waveforms(batch_nonlinear=True, runs=1):
    # Base path
    base_path = "D:/Audio/Source Absolute DivisiveSynthesisWaveforms"
    
    # Waveform types
    waveforms = ['sine', 'square', 'triangle']
    
    # Sample counts for first waveform (C1 to C4)
    sample_counts_wave1 = [
        1348, 1273, 1201, 1134, 1070, 1010, 953, 900, 849, 802, 757, 714,
        674, 636, 601, 567, 535, 505, 477, 450, 425, 401, 378, 357,
        337, 318, 300, 283, 268, 253, 238, 225, 212, 200, 189, 179,
        169, 159, 150, 142, 134, 126, 119, 113, 106, 100, 95, 89
    ]
    
    # Complete sample counts for second waveform (C1 to C6)
    sample_counts_wave2 = [
        5395, 5092, 4808, 4537, 4283, 4043, 3816, 3600, 3398, 3207, 3027, 2857,  # C-1 octave
        2697, 2546, 2404, 2269, 2141, 2021, 1908, 1800, 1699, 1604, 1514, 1429,  # C0 octave
        1348, 1273, 1201, 1134, 1070, 1010, 953, 900, 849, 802, 757, 714,        # C1 octave
        674, 636, 601, 567, 535, 505, 477, 450, 425, 401, 378, 357,              # C2 octave
        337, 318, 300, 283, 268, 253, 238, 225, 212, 200, 189, 179,              # C3 octave
        169, 159, 150, 142, 134, 126, 119, 113, 106, 100, 95, 89,                # C4 octave
        84, 80, 75, 71, 67, 63, 60, 56, 53, 50, 47, 45,                          # C5 octave
        42, 40, 38, 35, 33, 32, 30, 28, 27, 25, 24, 22                           # C6 octave
    ]
    
    # Generate note names (C1 to C4)
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note_names = []
    for oct in range(1, 5):  # C1 to C4
        note_names.extend([f"{note}{oct}" for note in notes])
    
    # Create all necessary directories and generate synthesis calls
    for power in range(2,9):

        power_dir = os.path.join(base_path, f"DivisivePower{power}")
        
        # Generate all waveform combinations
        for wave1, wave2 in product(waveforms, waveforms):
            separator = '÷'
            wave_combo_dir = os.path.join(power_dir, f"{wave1.capitalize()}{separator}{wave2.capitalize()}")
            
            # Generate folders for each semitone shift (-24 to +24)
            for semitone in range(-24, 25):
                semitone_dir = os.path.join(wave_combo_dir, f"{wave1.capitalize()}{separator}{wave2.capitalize()}S{semitone}")
                os.makedirs(semitone_dir, exist_ok=True)
                
                # Generate each note
                for note_idx, (note_name, sample1) in enumerate(zip(note_names, sample_counts_wave1)):
                    # Calculate the index for wave2 based on semitone shift
                    wave2_base_idx = 24  # Index of C1 in wave2 list (since we're starting from C1)
                    wave2_idx = wave2_base_idx + note_idx + semitone
                    
                    # Skip if the shifted index would be out of bounds
                    if wave2_idx < 0 or wave2_idx >= len(sample_counts_wave2):
                        continue
                    
                    sample2 = sample_counts_wave2[wave2_idx]
                    
                    # Generate multiple samples if requested
                    for run in range(1, runs + 1):
                        # Construct filename based on whether this is a multisample run
                        if runs == 1:
                            filename = f"{note_name}.wav"
                        else:
                            filename = f"{note_name} MS{run}.wav"
                        
                        output_path = os.path.join(semitone_dir, filename)
                        
                        # Execute the synthesis directly
                        synthesis_call = f"OperationalSynthesis.Divisive('{wave1}', {sample1}, 0.5, '{wave2}', {sample2}, 0.5, '{output_path}', divisive_power={power}, time=10, nonlinear={batch_nonlinear}, stereo=False, DVAbsolute=True)"
                        
                        try:
                            print(f"Generating: {synthesis_call}")
                            exec(synthesis_call)
                            print(f"Successfully generated: {output_path}")
                        except Exception as e:
                            print(f"Error generating {output_path}: {str(e)}")

def batch_null_synthesis_waveforms(batch_nonlinear=True, runs=4):
    """
    Generates single waveforms for each note and waveform type with optional multisampling.
    Covers 6 octaves from C1 to C6.
    
    Args:
        batch_nonlinear (bool): If True, uses NonLinearWaveforms, if False uses regular Waveforms
        runs (int): Number of times to generate each sample. If > 1, appends MS1, MS2, etc. to filenames
    """
    # Base path
    base_path = "D:/Audio/Unstable Oscillators/Null"
    
    # Waveform types
    waveforms = ['sine', 'square', 'triangle']
    
    # Sample counts (C1 to C6)
    sample_counts = [
        1348, 1273, 1201, 1134, 1070, 1010, 953, 900, 849, 802, 757, 714,        # C1 octave
        674, 636, 601, 567, 535, 505, 477, 450, 425, 401, 378, 357,              # C2 octave
        337, 318, 300, 283, 268, 253, 238, 225, 212, 200, 189, 179,              # C3 octave
        169, 159, 150, 142, 134, 126, 119, 113, 106, 100, 95, 89,                # C4 octave
        84, 80, 75, 71, 67, 63, 60, 56, 53, 50, 47, 45,                          # C5 octave
        42, 40, 38, 35, 33, 32, 30, 28, 27, 25, 24, 22                           # C6 octave
    ]
    
    # Generate note names (C1 to C6)
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note_names = []
    for oct in range(1, 7):  # C1 to C6
        note_names.extend([f"{note}{oct}" for note in notes])
    
    # Create directory structure and generate synthesis calls
    for wave in waveforms:
        # Create wave directory
        wave_dir = os.path.join(base_path, f"{wave.capitalize()}")
        os.makedirs(wave_dir, exist_ok=True)
        
        # Generate each note
        for note_name, sample_count in zip(note_names, sample_counts):
            # Generate multiple samples if requested
            for run in range(1, runs + 1):
                # Construct filename based on whether this is a multisample run
                if runs == 1:
                    filename = f"{note_name}.wav"
                else:
                    filename = f"{note_name} MS{run}.wav"
                
                output_path = os.path.join(wave_dir, filename)
                
                # Execute the synthesis directly
                synthesis_call = f"OperationalSynthesis.Null('{wave}', {sample_count}, 0.5, '{output_path}', time=10, nonlinear={batch_nonlinear}, stereo=False)"
                
                try:
                    print(f"Generating: {synthesis_call}")
                    exec(synthesis_call)
                    print(f"Successfully generated: {output_path}")
                except Exception as e:
                    print(f"Error generating {output_path}: {str(e)}")

#Debug Functions

def divisivepowervalues(divisive_power, wave_type='sine'):
    """
    Print the scaled divisive power values for a given waveform type and divisive power.
    
    Args:
        divisive_power (int): The divisive power to scale to
        wave_type (str): The type of waveform ('sine', 'square', or 'triangle')
    """
    # Generate a small sample of the chosen waveform
    if wave_type == 'sine':
        samples = Waveforms.sine(100, 0.5)  # One second of sine wave at max amplitude
    elif wave_type == 'square':
        samples = Waveforms.square(100, 0.5)
    elif wave_type == 'triangle':
        samples = Waveforms.triangle(100, 0.5)
    else:
        raise ValueError("Wave type must be 'sine', 'square', or 'triangle'")
    
    # Scale the samples using the same scaling function
    scaled_values = np.round(OperationalSynthesis._scale_to_bit_range(samples, divisive_power)).astype(int)
    
    # Print original and scaled values
    print(f"\nWaveform type: {wave_type}")
    print(f"Divisive power: {divisive_power}")
    print("\nFirst 10 original values:")
    print(samples[:10])
    print("\nFirst 10 scaled values:")
    print(scaled_values[:10])
    print(f"\nScaled value range: {np.min(scaled_values)} to {np.max(scaled_values)}")
    
    return scaled_values

#print (divisivepowervalues(3))




# Example usage:
# Single sample per note (default):
#batch_null_synthesis_waveforms(batch_nonlinear=True)

# Generate 4 multisamples per note:
#batch_null_synthesis_waveforms(batch_nonlinear=True, runs=3)

# Generate 8 linear multisamples per note:
#batch_null_synthesis_waveforms(batch_nonlinear=False, runs=1)
#batch_divisive_synthesis_waveforms(batch_nonlinear=False, runs=1)