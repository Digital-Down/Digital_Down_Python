class Methylphenethylamine:
    @classmethod
    def slow(cls, samples_list, iterations):
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
    def fast(cls, samples_list, iterations):
        samples = samples_list[0]  # Extract the inner list of samples
        for _ in range(iterations):
            samples = [samples[i] for i in range(len(samples)) if i % 2 == 0]
        return [samples]
