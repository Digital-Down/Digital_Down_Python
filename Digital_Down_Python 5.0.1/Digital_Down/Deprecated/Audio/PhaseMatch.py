import os
from .AudioSampleValues import AudioSampleValues
import numpy as np

class PhaseMatch:
    @staticmethod
    def PhaseMatch(source_path, target_path, threshold=100):
        print(f"Starting phase matching process...")
        print(f"Source: {source_path}")
        print(f"Target: {target_path}")
        print(f"Threshold: {threshold}")

        # Check if files exist
        if not os.path.exists(source_path) or not os.path.exists(target_path):
            raise FileNotFoundError("One or both of the specified files do not exist.")

        # Get sample values as lists
        source_samples = AudioSampleValues.wav_to_list(source_path)
        target_samples = AudioSampleValues.wav_to_list(target_path)

        print(f"Source samples shape: {np.array(source_samples).shape}")
        print(f"Target samples shape: {np.array(target_samples).shape}")

        # Ensure both audio files have the same number of channels
        if len(source_samples[0]) != len(target_samples[0]):
            raise ValueError("Source and target audio files must have the same number of channels.")





        # Convert to numpy arrays for efficient processing
        source_array = np.array(source_samples)
        target_array = np.array(target_samples)

        # Apply phase matching
        changes_made = 0
        total_samples = 0
        samples_above_threshold = 0

        for channel in range(source_array.shape[1]):
            source_channel = source_array[:, channel]
            target_channel = target_array[:, channel]

            # Create masks for samples above the threshold
            source_mask = np.abs(source_channel) > threshold

            samples_above_threshold += np.sum(source_mask)
            total_samples += len(source_channel)

            # Store original signs of target samples
            original_signs = np.sign(target_channel[source_mask])

            # Apply phase matching
            new_target = np.abs(target_channel[source_mask]) * np.sign(source_channel[source_mask])
            
            # Count changes made
            changes_made += np.sum(original_signs != np.sign(new_target))

            # Update target_array with new values
            target_array[source_mask, channel] = new_target

        # Convert back to list
        processed_samples = target_array.tolist()

        # Generate output filename
        base, ext = os.path.splitext(target_path)
        output_path = f"{base} PhaseMatched{ext}"

        # Save the processed audio
        AudioSampleValues.list_to_wav(processed_samples, output_path)

        print(f"Phase matching complete.")
        print(f"Total samples: {total_samples}")
        print(f"Samples above threshold: {samples_above_threshold}")
        print(f"Changes made: {changes_made}")
        print(f"Percentage of samples above threshold: {(samples_above_threshold / total_samples) * 100:.2f}%")
        print(f"Percentage of samples changed: {(changes_made / samples_above_threshold) * 100:.2f}% (of samples above threshold)")
        print(f"Phase-matched audio saved to: {output_path}")

        return changes_made, samples_above_threshold, total_samples

# Example usage:
# changes, processed, total = PhaseMatch.PhaseMatch('source_file_path.wav', 'target_file_path.wav', threshold=100)
# print(f"Changes made: {changes}/{processed} samples (out of {total} total samples)")



input = 'D:/5th Generation (When Desktop Is Full)/Audio/Stems and Mixes for Future Edits/Normalized Stems/Incunabula/Incunabula/Bass.wav'
process = 'D:/5th Generation (When Desktop Is Full)/Audio/Stems and Mixes for Future Edits/Normalized Stems/Incunabula/Incunabula/808 Kicks.wav'
# Example usage:
PhaseMatch.PhaseMatch(process, input, threshold=1000)

# there are two script in claude, one is a different phase allignment, the other is the same as above but with padding 0s to match lengths.