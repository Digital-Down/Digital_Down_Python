import os
import librosa
import numpy as np

class MeasurePitch:
    def __init__(self):
        # Dictionary to map frequencies to musical notes, now starting from C-2
        self.notes = {
            'C': [4.0879, 8.176, 16.35, 32.70, 65.41, 130.81, 261.63, 523.25, 1046.50, 2093.00, 4186.01],
            'C#/Db': [4.331, 8.662, 17.32, 34.65, 69.30, 138.59, 277.18, 554.37, 1108.73, 2217.46, 4434.92],
            'D': [4.5885, 9.177, 18.35, 36.71, 73.42, 146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.64],
            'D#/Eb': [4.8615, 9.723, 19.45, 38.89, 77.78, 155.56, 311.13, 622.25, 1244.51, 2489.02, 4978.03],
            'E': [5.1505, 10.301, 20.60, 41.20, 82.41, 164.81, 329.63, 659.26, 1318.51, 2637.02, 5274.04],
            'F': [5.457, 10.914, 21.83, 43.65, 87.31, 174.61, 349.23, 698.46, 1396.91, 2793.83, 5587.65],
            'F#/Gb': [5.7815, 11.563, 23.12, 46.25, 92.50, 185.00, 369.99, 739.99, 1479.98, 2959.96, 5919.91],
            'G': [6.125, 12.250, 24.50, 49.00, 98.00, 196.00, 392.00, 783.99, 1567.98, 3135.96, 6271.93],
            'G#/Ab': [6.4895, 12.979, 25.96, 51.91, 103.83, 207.65, 415.30, 830.61, 1661.22, 3322.44, 6644.88],
            'A': [6.875, 13.750, 27.50, 55.00, 110.00, 220.00, 440.00, 880.00, 1760.00, 3520.00, 7040.00],
            'A#/Bb': [7.284, 14.568, 29.14, 58.27, 116.54, 233.08, 466.16, 932.33, 1864.66, 3729.31, 7458.62],
            'B': [7.717, 15.434, 30.87, 61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07, 7902.13]
        }

    def find_nearest_note(self, frequency):
        if frequency <= 0:
            return None, None, None
            
        min_diff_ratio = float('inf')
        nearest_note = None
        nearest_freq = None
        octave = None

        for note, frequencies in self.notes.items():
            for i, freq in enumerate(frequencies):
                # Use frequency ratio for comparison instead of absolute difference
                ratio = frequency / freq
                log_ratio = abs(np.log2(ratio))
                
                if log_ratio < min_diff_ratio:
                    min_diff_ratio = log_ratio
                    nearest_note = note
                    nearest_freq = freq
                    octave = i - 2  # Adjust octave to start from -2 instead of 0

        # If the frequency is too far from any note (more than a quarter step),
        # we might have a detection error
        if min_diff_ratio > 0.5:  # roughly a quarter tone
            return None, None, None
            
        return f"{nearest_note}{octave}", nearest_freq, frequency

    def filepitch(self, audio_path):
        """Analyze a single audio file and return its pitch information."""
        try:
            print(f"Processing: {os.path.basename(audio_path)}")
            
            # Load the audio file with a lower sampling rate for better low-frequency resolution
            y, sr = librosa.load(audio_path, sr=22050)
            
            # Apply some preprocessing
            y = librosa.effects.preemphasis(y)
            
            # Get pitch using multiple estimation methods
            f0_1, voiced_flag, voiced_probs = librosa.pyin(y, 
                                                         fmin=librosa.note_to_hz('C-2'),
                                                         fmax=librosa.note_to_hz('C7'),
                                                         sr=sr)
            
            # Filter out unvoiced sections and zero values
            f0_1 = f0_1[voiced_flag & (f0_1 > 0)]
            
            if len(f0_1) == 0:
                print(f"No pitch detected for: {os.path.basename(audio_path)}")
                return "Unknown", None, None
                
            # Take the median of the detected pitches to avoid outliers
            pitch = np.median(f0_1)
            
            # Find the nearest musical note
            note, standard_freq, detected_freq = self.find_nearest_note(pitch)
            
            # If we couldn't determine the note, try to infer it from the filename
            if note is None:
                # Try to extract note information from filename
                filename = os.path.basename(audio_path)
                note_name = filename.split('.')[0]  # Remove extension
                try:
                    # Attempt to get frequency from librosa
                    standard_freq = librosa.note_to_hz(note_name)
                    note = note_name
                    detected_freq = pitch
                except:
                    print(f"Could not determine pitch for: {os.path.basename(audio_path)}")
                    return "Unknown", None, None
            
            print(f"Found {note} (Standard: {standard_freq:.2f} Hz, Detected: {detected_freq:.2f} Hz)")
            return note, standard_freq, detected_freq
            
        except Exception as e:
            print(f"Error processing {os.path.basename(audio_path)}: {str(e)}")
            return f"Error processing {audio_path}: {str(e)}", None, None

    def batchpitch(self, root_directory, output_file="Divisive Frequency Measurements.txt"):
        """Analyze all audio files in a directory hierarchy and save results to a text file."""
        audio_extensions = {'.wav', '.mp3', '.flac', '.ogg', '.m4a'}
        
        print(f"\nStarting analysis of directory: {root_directory}")
        total_files = sum(len([f for f in files if os.path.splitext(f)[1].lower() in audio_extensions]) 
                         for _, _, files in os.walk(root_directory))
        processed_files = 0
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for root, dirs, files in os.walk(root_directory):
                # Calculate relative path for indentation
                level = root.replace(root_directory, '').count(os.sep)
                indent = '    ' * level
                
                # Write directory name
                if level > 0:  # Skip root directory name
                    f.write(f"{indent}{os.path.basename(root)}/\n")
                    print(f"\nProcessing directory: {os.path.basename(root)}")
                
                # Process audio files in current directory
                audio_files = [file for file in files if os.path.splitext(file)[1].lower() in audio_extensions]
                
                # Group files by note
                note_groups = {}
                for audio_file in audio_files:
                    file_path = os.path.join(root, audio_file)
                    note, standard_freq, detected_freq = self.filepitch(file_path)
                    
                    if note not in note_groups:
                        note_groups[note] = []
                    note_groups[note].append((audio_file, standard_freq, detected_freq))
                    
                    processed_files += 1
                    print(f"Progress: {processed_files}/{total_files} files processed ({(processed_files/total_files*100):.1f}%)")
                
                # Write grouped results
                for note in sorted(note_groups.keys()):
                    if note != "Unknown" and not note.startswith("Error"):
                        f.write(f"{indent}    {note}:\n")
                        for audio_file, standard_freq, detected_freq in sorted(note_groups[note]):
                            f.write(f"{indent}        {audio_file} - Standard: {standard_freq:.2f} Hz, Detected: {detected_freq:.2f} Hz\n")
                
                if audio_files:
                    f.write('\n')  # Add spacing between directories
        
        print(f"\nAnalysis complete! Results saved to {output_file}")

def main():
    # Example usage
    analyzer = MeasurePitch()
    
    # Single file analysis
    #note, freq = analyzer.filepitch("path/to/audio/file.wav")
    #print(f"Single file analysis: {note} - {freq:.2f} Hz")
    
    # Batch analysis
    analyzer.batchpitch("D:/Audio/Source DivisiveSynthesisWaveforms/DivisivePower2/Sine÷Sine", )
    print("Batch analysis completed. Results saved to pitch_analysis.txt")

#if __name__ == "__main__":
#    main()