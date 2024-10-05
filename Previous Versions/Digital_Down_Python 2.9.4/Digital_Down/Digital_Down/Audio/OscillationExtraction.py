import numpy as np

class OscillationExtraction:
    @staticmethod
    def fullphase(audio_data, channel=0, LowSamplePhaseCount=5, LSPCOperation='omit'):
        current_oscillation = []
        oscillations = []
        positive_count = 0
        negative_count = 0
        state = 'positive'
        
        print(f"Starting SFT with LowSamplePhaseCount={LowSamplePhaseCount}, LSPCOperation={LSPCOperation}")

        for i, sample in enumerate(audio_data):
            value = sample[channel]

            if state == 'positive':
                if value > 0:
                    positive_count += 1
                    current_oscillation.append(value)
                elif value < 0:
                    # Check if positive phase should be processed
                    if positive_count <= LowSamplePhaseCount:
                        print(f"Low positive count detected: {positive_count}")
                        if LSPCOperation == 'omit':
                            print("Omitting low positive count samples")
                            current_oscillation = current_oscillation[:-positive_count]
                            positive_count = 0
                        elif LSPCOperation == 'ignore':
                            print("Ignoring low positive count")
                            # Do nothing, keep the samples but don't count them
                            positive_count = 0
                    
                    state = 'negative'
                    negative_count = 1
                    current_oscillation.append(value)
                else:  # value == 0
                    current_oscillation.append(value)
            else:  # state == 'negative'
                if value < 0:
                    negative_count += 1
                    current_oscillation.append(value)
                elif value > 0:
                    # Check if negative phase should be processed
                    if negative_count <= LowSamplePhaseCount:
                        print(f"Low negative count detected: {negative_count}")
                        if LSPCOperation == 'omit':
                            print("Omitting low negative count samples")
                            current_oscillation = current_oscillation[:-negative_count]
                            negative_count = 0
                        elif LSPCOperation == 'ignore':
                            print("Ignoring low negative count")
                            # Do nothing, keep the samples but don't count them
                            negative_count = 0

                    # Check if we've completed a full oscillation
                    if positive_count > 0 and negative_count > 0:
                        oscillations.append({
                            'samples': current_oscillation,
                            'positive_count': positive_count,
                            'negative_count': negative_count
                        })
                        print(f"Oscillation detected: positive_count={positive_count}, negative_count={negative_count}")
                    
                    # Reset for the next oscillation
                    state = 'positive'
                    positive_count = 1
                    negative_count = 0
                    current_oscillation = [value]
                else:  # value == 0
                    current_oscillation.append(value)

            if i % 10000 == 0:
                print(f"Processed {i} samples")

        print(f"SFT completed. Total oscillations detected: {len(oscillations)}")
        return oscillations

    @staticmethod
    def singlephase(audio_data, channel=0, phase='positive', LowSamplePhaseCount=5, LSPCOperation='omit'):
        current_oscillation = []
        oscillations = []
        positive_count = 0
        negative_count = 0
        
        print(f"Starting SinglePhaseSFT with phase={phase}, LowSamplePhaseCount={LowSamplePhaseCount}, LSPCOperation={LSPCOperation}")

        for i, sample in enumerate(audio_data):
            value = sample[channel]

            if value > 0:
                positive_count += 1
                current_oscillation.append(value)
            elif value < 0:
                negative_count += 1
                current_oscillation.append(value)
            else:  # value == 0
                current_oscillation.append(value)

            # Check if we've completed a half oscillation
            if (phase == 'positive' and value <= 0 and positive_count > 0) or \
               (phase == 'negative' and value >= 0 and negative_count > 0):
                
                count_to_check = positive_count if phase == 'positive' else negative_count
                
                if count_to_check <= LowSamplePhaseCount:
                    print(f"Low {phase} count detected: {count_to_check}")
                    if LSPCOperation == 'omit':
                        print(f"Omitting low {phase} count samples")
                        current_oscillation = current_oscillation[:-count_to_check]
                        if phase == 'positive':
                            positive_count = 0
                        else:
                            negative_count = 0
                    elif LSPCOperation == 'ignore':
                        print(f"Ignoring low {phase} count")
                        # Do nothing, keep the samples but don't count them
                        if phase == 'positive':
                            positive_count = 0
                        else:
                            negative_count = 0
                
                if (phase == 'positive' and positive_count > 0) or (phase == 'negative' and negative_count > 0):
                    oscillations.append({
                        'samples': current_oscillation,
                        'positive_count': positive_count,
                        'negative_count': negative_count
                    })
                    print(f"Half oscillation detected: positive_count={positive_count}, negative_count={negative_count}")

                # Reset for the next oscillation
                positive_count = 0
                negative_count = 0
                current_oscillation = []

            if i % 10000 == 0:
                print(f"Processed {i} samples")

        print(f"SinglePhaseSFT completed. Total half oscillations detected: {len(oscillations)}")
        return oscillations