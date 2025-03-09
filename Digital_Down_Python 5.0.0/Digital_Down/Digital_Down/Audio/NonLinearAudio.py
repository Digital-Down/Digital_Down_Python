import random

def apply_nonlinearity(samples, nonlinearity):
    nonlinearity = round(nonlinearity)  # Round to nearest integer
    return [
        sample + random.randint(-nonlinearity, nonlinearity)
        for sample in samples
    ]

def apply_temporal_changes(samples, temporal_chance):
    temporal_chance = round(temporal_chance)  # Round to nearest integer
    result = []
    for i in range(len(samples) - 1):
        result.append(samples[i])
        if random.randint(0, 99) < temporal_chance:
            if random.choice([True, False]):  # 50% chance to add or remove
                # Add a sample
                new_sample = (samples[i] + samples[i+1]) // 2
                result.append(new_sample)
            else:
                # Remove next sample
                i += 1
    result.append(samples[-1])  # Add the last sample
    return result