class CompositionTools:
    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    POSITIONS = ['root', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    
    @classmethod
    def _get_scale(cls, scale_root, intervals, position=None):
        if scale_root not in cls.NOTES:
            raise ValueError(f"Invalid root note. Please use one of: {', '.join(cls.NOTES)}")
        
        root_index = cls.NOTES.index(scale_root)
        scale = [cls.NOTES[(root_index + interval) % 12] for interval in intervals]
        
        if position is None:
            return scale
        elif position in cls.POSITIONS[:len(scale)]:
            return scale[cls.POSITIONS.index(position)]
        else:
            raise ValueError(f"Invalid position. Please use one of: {', '.join(cls.POSITIONS[:len(scale)])}")
    
    @classmethod
    def Scales(cls, scale_root, scale_type="Ionian", position=None):
        # Get the scale method
        method_name = f"_scale_{scale_type}"
        scale_method = getattr(cls, method_name, None)
        
        if scale_method is None:
            raise ValueError(f"Invalid scale type: {scale_type}")
        
        return scale_method(scale_root, position)
    
    @classmethod
    def Chords(cls, scale_root, chord="maj"):
        # Get the chord method
        method_name = f"_chord_{chord}"
        chord_method = getattr(cls, method_name, None)
        
        if chord_method is None:
            raise ValueError(f"Invalid chord type: {chord}")
        
        return chord_method(scale_root)
    
    @classmethod
    def ChordsInScale(cls, scale_letter, scale_type, position=None):
        # Get the scale
        scale = cls.Scales(scale_letter, scale_type)
        
        # Get all chord methods
        chord_methods = [method.replace('_chord_', '') for method in dir(cls) if method.startswith('_chord_')]
        
        positions = [position] if position else cls.POSITIONS[:len(scale)]
        
        result = {}
        result[f"Chords in {scale_letter} {scale_type}:"] = {}
        
        for pos in positions:
            pos_index = cls.POSITIONS.index(pos) if pos in cls.POSITIONS else int(pos)
            root_note = scale[pos_index % len(scale)]
            
            compatible_chords = []
            for chord_method in chord_methods:
                chord = cls.Chords(root_note, chord_method)
                if all(note in scale for note in chord):
                    compatible_chords.append((root_note, chord_method, chord))
            
            result[f"Chords in {scale_letter} {scale_type}:"][f"{pos.capitalize()}:"] = []
            for root_note, chord_method, chord in compatible_chords:
                result[f"Chords in {scale_letter} {scale_type}:"][f"{pos.capitalize()}:"].append(f"{root_note} {chord_method}: {', '.join(chord)}")
        
        return result
    
    # Scale methods
    @classmethod
    def _scale_Ionian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 9, 11], position)

    @classmethod
    def _scale_Dorian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 9, 10], position)

    @classmethod
    def _scale_Phrygian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 7, 8, 10], position)

    @classmethod
    def _scale_Lydian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 7, 9, 11], position)

    @classmethod
    def _scale_Mixolydian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 9, 10], position)

    @classmethod
    def _scale_Aeolian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 8, 10], position)

    @classmethod
    def _scale_Locrian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 6, 8, 10], position)

    @classmethod
    def _scale_Ultralocrian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 4, 6, 8, 9], position)

    @classmethod
    def _scale_Superlocrian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 4, 6, 8, 10], position)

    @classmethod
    def _scale_MelodicMinor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 9, 11], position)

    @classmethod
    def _scale_DorianFlat2(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 7, 9, 10], position)

    @classmethod
    def _scale_LydianAugmented(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 8, 9, 11], position)

    @classmethod
    def _scale_LydianDominant(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 7, 9, 10], position)

    @classmethod
    def _scale_MixolydianFlat6(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 8, 10], position)

    @classmethod
    def _scale_LocrianSharp2(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 6, 8, 10], position)

    @classmethod
    def _scale_AlteredDominant(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 4, 6, 8, 10], position)

    @classmethod
    def _scale_HarmonicMinor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 8, 11], position)

    @classmethod
    def _scale_LocrianNatural6(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 6, 9, 10], position)

    @classmethod
    def _scale_IonianSharp5(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 8, 9, 11], position)

    @classmethod
    def _scale_DorianSharp4(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 6, 7, 9, 10], position)

    @classmethod
    def _scale_PhrygianMajor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 7, 8, 10], position)

    @classmethod
    def _scale_LydianSharp2(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 3, 4, 6, 7, 9, 11], position)

    @classmethod
    def _scale_SuperlocrianDoubleFlat7(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 4, 6, 8, 9], position)

    @classmethod
    def _scale_MajorPentatonic(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 7, 9], position)

    @classmethod
    def _scale_MinorPentatonic(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 3, 5, 7, 10], position)

    @classmethod
    def _scale_EgyptianPentatonic(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 5, 7, 10], position)

    @classmethod
    def _scale_BluesScale(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 3, 5, 6, 7, 10], position)

    @classmethod
    def _scale_MajorBluesScale(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 4, 7, 9], position)

    @classmethod
    def _scale_BebopDominant(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 9, 10, 11], position)

    @classmethod
    def _scale_BebopMajor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 8, 9, 11], position)

    @classmethod
    def _scale_BebopMinor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 4, 5, 7, 9, 10], position)

    @classmethod
    def _scale_BebopHarmonicMinor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 8, 9, 11], position)

    @classmethod
    def _scale_DoubleHarmonic(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 7, 8, 11], position)

    @classmethod
    def _scale_NeapolitanMinor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 7, 8, 11], position)

    @classmethod
    def _scale_NeapolitanMajor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 7, 9, 11], position)

    @classmethod
    def _scale_HungarianMinor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 6, 7, 8, 11], position)

    @classmethod
    def _scale_HungarianMajor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 3, 4, 6, 7, 9, 10], position)

    @classmethod
    def _scale_Enigmatic(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 6, 8, 10, 11], position)

    @classmethod
    def _scale_PersianScale(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 6, 8, 11], position)

    @classmethod
    def _scale_ArabicScale(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 7, 8, 11], position)

    @classmethod
    def _scale_TodiTheta(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 6, 7, 8, 11], position)

    @classmethod
    def _scale_WholeTone(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 8, 10], position)

    @classmethod
    def _scale_Diminished(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 6, 8, 9, 11], position)

    @classmethod
    def _scale_DominantDiminished(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 4, 6, 7, 9, 10], position)

    @classmethod
    def _scale_Chromatic(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], position)

    @classmethod
    def _scale_Algerian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 6, 7, 8, 11], position)

    @classmethod
    def _scale_AugmentedScale(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 3, 4, 7, 8, 11], position)

    @classmethod
    def _scale_Balinese(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 7, 8], position)

    @classmethod
    def _scale_Byzantine(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 7, 8, 11], position)

    @classmethod
    def _scale_Chinese(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 7, 9], position)

    @classmethod
    def _scale_Hirajoshi(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 7, 8], position)

    @classmethod
    def _scale_InSen(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 5, 7, 10], position)

    @classmethod
    def _scale_Iwato(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 5, 6, 10], position)

    @classmethod
    def _scale_Kumoi(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 7, 9], position)

    @classmethod
    def _scale_Pelog(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 7, 8], position)

    @classmethod
    def _scale_Prometheus(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 9, 10], position)

    @classmethod
    def _scale_SixToneSymmetrical(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 8, 9], position)

    @classmethod
    def _scale_Yo(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 5, 7, 9], position)

    @classmethod
    def _scale_Akebono(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 7, 9], position)

    @classmethod
    def _scale_Asavari(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 8, 10], position)

    # Chord methods
    @classmethod
    def _chord_aug(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 8])
    
    @classmethod
    def _chord_aug11th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 7, 10])
    
    @classmethod
    def _chord_augmaj7th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 8, 11])
    
    @classmethod
    def _chord_aug7th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 8, 10])
    
    @classmethod
    def _chord_aug6thitalian(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 10])
    
    @classmethod
    def _chord_aug6thfrench(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 6, 10])
    
    @classmethod
    def _chord_aug6thgerman(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 7, 10])
    
    @classmethod
    def _chord_dim(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 6])
    
    @classmethod
    def _chord_dimmaj7th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 6, 10])
    
    @classmethod
    def _chord_dim7th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 6, 9])
    
    @classmethod
    def _chord_dom11th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 10])
    
    @classmethod
    def _chord_dommin9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 4, 7, 10])
    
    @classmethod
    def _chord_dom9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 7, 10])
    
    @classmethod
    def _chord_min(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 7])
    
    @classmethod
    def _chord_dom7thsharp9(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 4, 7, 10])
    
    @classmethod
    def _chord_dom13th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 9, 10])
    
    @classmethod
    def _chord_dream(cls, scale_root):
        return cls._get_scale(scale_root, [0, 5, 6, 7])
    
    @classmethod
    def _chord_elektra(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 4, 7, 9])
    
    @classmethod
    def _chord_farben(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 8, 9, 11])
    
    @classmethod
    def _chord_lydian(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 6, 7, 11])
    
    @classmethod
    def _chord_magic(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 6, 10])
    
    @classmethod
    def _chord_maj(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 7])
    
    @classmethod
    def _chord_maj11th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 11])
    
    @classmethod
    def _chord_maj7th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 7, 11])
    
    @classmethod
    def _chord_maj7thsharp11(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 6, 8, 11])
    
    @classmethod
    def _chord_maj6th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 7, 9])
    
    @classmethod
    def _chord_maj6th9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 7, 9])
    
    @classmethod
    def _chord_maj9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 7, 11])
    
    @classmethod
    def _chord_maj13th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 9, 11])
    
    @classmethod
    def _chord_min11th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 10])
    
    @classmethod
    def _chord_min7th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 7, 10])
    
    @classmethod
    def _chord_min9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 3, 7, 10])
    
    @classmethod
    def _chord_min6th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 7, 9])
    
    @classmethod
    def _chord_min6th9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 3, 7, 9])
    
    @classmethod
    def _chord_min13th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 9, 10])
    
    @classmethod
    def _chord_mystic(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 9, 10])
    
    @classmethod
    def _chord_neapolitan(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 5, 8])
    
    @classmethod
    def _chord_ninethaug5th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 7, 8, 10])
    
    @classmethod
    def _chord_northernlights(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 2, 3, 4, 6, 7, 8, 10, 11])
    
    @classmethod
    def _chord_hexa(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 8, 9])
    
    @classmethod
    def _chord_petrushka(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 4, 6, 7, 10])
    
    @classmethod
    def _chord_power(cls, scale_root):
        return cls._get_scale(scale_root, [0, 7])
    
    @classmethod
    def _chord_sevensix(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 7, 9, 10])
    
    @classmethod
    def _chord_seventhsus4(cls, scale_root):
        return cls._get_scale(scale_root, [0, 5, 7, 10])
    
    @classmethod
    def _chord_sowhat(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 5, 7, 10])
    
    @classmethod
    def _chord_thirteenthflat9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 4, 7, 9, 10])
    
    @classmethod
    def _chord_thirteenthflat9thflat5th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 4, 6, 9, 10])
    
    @classmethod
    def _chord_viennese1(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 6])
    
    @classmethod
    def _chord_viennese2(cls, scale_root):
        return cls._get_scale(scale_root, [0, 6, 7])