from .Scales import *
from .Chords import *

class CompositionTools:
    @staticmethod
    def chords_in_scale(scale_letter, scale_type, position=None):
        # Get the scale
        scale_method = getattr(Scales, scale_type, None)
        if scale_method is None:
            raise ValueError(f"Invalid scale type: {scale_type}")
        
        scale = scale_method(scale_letter)
        
        # Get all chord methods
        chord_methods = [method for method in dir(Chords) if callable(getattr(Chords, method)) and not method.startswith("_")]
        
        positions = [position] if position else Scales.POSITIONS[:len(scale)]
        
        print(f"Chords in {scale_letter} {scale_type}:")
        for pos in positions:
            pos_index = Scales.POSITIONS.index(pos)
            root_note = scale[pos_index % len(scale)]
            
            compatible_chords = []
            for chord_method in chord_methods:
                chord_func = getattr(Chords, chord_method)
                chord = chord_func(root_note)
                if all(note in scale for note in chord):
                    compatible_chords.append((root_note, chord_method, chord))
            
            print(f"\n{pos.capitalize()}:")
            for root_note, chord_method, chord in compatible_chords:
                print(f"  - {root_note} {chord_method}: {', '.join(chord)}")