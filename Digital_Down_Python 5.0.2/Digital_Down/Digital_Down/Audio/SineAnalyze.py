import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft

def sineanalyze(file_path, amplitude_threshold=0.05):
    """
    Analyze audio file and return main sine wave components
    Returns only frequencies with amplitude above threshold, sorted by amplitude
    """
    # Read the wav file
    sample_rate, data = wavfile.read(file_path)
    
    # If stereo, convert to mono
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)
    
    # Perform FFT
    fft_result = fft(data)
    frequencies = np.fft.fftfreq(len(data), 1/sample_rate)
    amplitudes = np.abs(fft_result)
    
    # Get positive frequencies only
    positive_mask = frequencies > 0
    frequencies = frequencies[positive_mask]
    amplitudes = amplitudes[positive_mask]
    
    # Normalize amplitudes
    amplitudes = amplitudes / np.max(amplitudes)
    
    # Filter out low amplitudes and sort by amplitude
    significant_mask = amplitudes > amplitude_threshold
    frequencies = frequencies[significant_mask]
    amplitudes = amplitudes[significant_mask]
    
    # Sort by amplitude (highest first)
    sort_idx = np.argsort(amplitudes)[::-1]
    frequencies = frequencies[sort_idx]
    amplitudes = amplitudes[sort_idx]
    
    return frequencies, amplitudes

def main():
    file_path = "D:/5th Generation (When Desktop Is Full)/Audio/Corporate Sounds/90sSampleCDs/90ssamplecds/90s_sample_cds_converts/InVision Interactive - The Piano/InVision Interactive - The Piano/Partition A/BOESPLAYHARD/15BPHL3C  -R.wav"
    
    freqs, amps = sineanalyze(file_path, amplitude_threshold=0.05)
    
    print("\nMain sine components (frequency, amplitude):")
    print("-" * 40)
    for freq, amp in zip(freqs, amps):
        print(f"{freq:7.1f} Hz, {amp:.3f}")

#if __name__ == "__main__":
#    main()