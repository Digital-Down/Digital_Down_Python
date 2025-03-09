import math
import random
from .NonLinearAudio import apply_nonlinearity, apply_temporal_changes

class NonLinearWaveforms:
    @staticmethod
    def sine(length, amplitude, nonlinearity=0, temporal_chance=0):
        max_amplitude = 32767  # Maximum value for 16-bit signed integer
        samples = []
        
        for i in range(length):
            # Calculate the sine value
            value = math.sin(2 * math.pi * i / length)
            
            # Scale to 16-bit range and adjust amplitude
            scaled_value = int(round(value * max_amplitude * amplitude))
            
            samples.append(scaled_value)
        
        samples = apply_nonlinearity(samples, nonlinearity)
        samples = apply_temporal_changes(samples, temporal_chance)
        return samples

    @staticmethod
    def square(length, amplitude, nonlinearity=0, temporal_chance=0):
        max_amplitude = 32767
        samples = []
        
        for i in range(length):
            # Generate square wave
            value = 1 if i < length / 2 else -1
            
            scaled_value = int(round(value * max_amplitude * amplitude))
            samples.append(scaled_value)
        
        samples = apply_nonlinearity(samples, nonlinearity)
        samples = apply_temporal_changes(samples, temporal_chance)
        return samples

    @staticmethod
    def triangle(length, amplitude, nonlinearity=0, temporal_chance=0):
        max_amplitude = 32767
        samples = []
        
        for i in range(length):
            # Generate triangle wave
            value = 4 * abs(i / length - 0.5) - 1
            
            scaled_value = int(round(value * max_amplitude * amplitude))
            samples.append(scaled_value)
        
        samples = apply_nonlinearity(samples, nonlinearity)
        samples = apply_temporal_changes(samples, temporal_chance)
        return samples

    @staticmethod
    def sawtooth(length, amplitude, nonlinearity=0, temporal_chance=0):
        max_amplitude = 32767
        samples = []
        
        for i in range(length):
            # Generate sawtooth wave
            value = 2 * (i / length) - 1
            
            scaled_value = int(round(value * max_amplitude * amplitude))
            samples.append(scaled_value)
        
        samples = apply_nonlinearity(samples, nonlinearity)
        samples = apply_temporal_changes(samples, temporal_chance)
        return samples

    @staticmethod
    def pulse(length, amplitude, duty_cycle=0.5, nonlinearity=0, temporal_chance=0):
        if not 0 < duty_cycle < 1:
            raise ValueError("Duty cycle must be between 0 and 1")
        
        max_amplitude = 32767
        samples = []
        
        for i in range(length):
            # Generate pulse wave
            value = 1 if i / length < duty_cycle else -1
            
            scaled_value = int(round(value * max_amplitude * amplitude))
            samples.append(scaled_value)
        
        samples = apply_nonlinearity(samples, nonlinearity)
        samples = apply_temporal_changes(samples, temporal_chance)
        return samples

    @staticmethod
    def noise(length, amplitude, nonlinearity=0, temporal_chance=0):
        max_amplitude = 32767
        samples = []
        
        for _ in range(length):
            # Generate white noise
            value = random.uniform(-1, 1)
            
            scaled_value = int(round(value * max_amplitude * amplitude))
            samples.append(scaled_value)
        
        samples = apply_nonlinearity(samples, nonlinearity)
        samples = apply_temporal_changes(samples, temporal_chance)
        return samples