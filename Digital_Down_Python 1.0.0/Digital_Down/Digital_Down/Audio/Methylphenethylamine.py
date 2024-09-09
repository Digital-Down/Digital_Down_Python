class Methylphenethylamine:
    @classmethod
    def slow(cls, samples_list, iterations):
        """
        Slow down the audio by inserting new samples between existing ones.
        
        Parameters:
        samples_list (list of list of lists): A list containing a list of stereo values, where each stereo value is a list of two integers.
        iterations (int): The number of iterations to apply the slowing operation.
        Returns:
        list of list of lists: The modified list with inserted samples.
        """
        samples = samples_list[0]  # Extract the inner list of samples
        def interpolate(a, b):
            return [round((a[0] + b[0]) / 2), round((a[1] + b[1]) / 2)]
        for _ in range(iterations):
            new_samples = []
            for i in range(len(samples) - 1):
                new_samples.append(samples[i])
                new_samples.append(interpolate(samples[i], samples[i + 1]))
            new_samples.append(samples[-1])
            samples = new_samples
        
        return [samples]  # Wrap the result back in a list

    @classmethod
    def fast(cls, samples_list, iterations):
        """
        Speed up the audio by removing every even sample.
        Parameters:
        samples_list (list of list of lists): A list containing a list of stereo values, where each stereo value is a list of two integers.
        iterations (int): The number of iterations to apply the speeding operation.
        Returns:
        list of list of lists: The modified list with samples removed.
        """
        samples = samples_list[0]  # Extract the inner list of samples
        for _ in range(iterations):
            samples = [samples[i] for i in range(len(samples)) if i % 2 == 0]
        
        return [samples]  # Wrap the result back in a list
#Fast acceptable range is 1-6
#Slow acceptable range is 1
