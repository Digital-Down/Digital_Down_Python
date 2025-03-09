from .AudioSampleValues import *

class Methylphenethylamine:
    @classmethod
    def MSlow(cls, samples_list):
        iterations = 0
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
        return samples

    @classmethod
    def MFast(cls, samples_list):
        samples = samples_list[0]  # Extract the inner list of samples
        for _ in range(1):  # Fixed iteration count of 2
            samples = [samples[i] for i in range(len(samples)) if i % 2 == 0]
        return samples

    @classmethod
    def BatchMSlow(cls, input_folder, output_folder):
        cls._batch_process(input_folder, output_folder, cls.MSlow)

    @classmethod
    def BatchMFast(cls, input_folder, output_folder):
        cls._batch_process(input_folder, output_folder, cls.MFast)

    @classmethod
    def _batch_process(cls, input_folder, output_folder, process_method):
        for root, _, files in os.walk(input_folder):
            for file in files:
                if file.lower().endswith('.wav'):
                    input_path = os.path.join(root, file)
                    relative_path = os.path.relpath(input_path, input_folder)
                    output_path = os.path.join(output_folder, relative_path)
                    
                    # Create output directory if it doesn't exist
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    
                    # Process the file
                    input_samples = AudioSampleValues.wav_to_list(input_path)
                    processed_samples = process_method([input_samples])
                    AudioSampleValues.list_to_wav(processed_samples, output_path)
                    print(f"Processed: {input_path} -> {output_path}")

