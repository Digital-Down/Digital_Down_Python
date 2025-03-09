class Scales:
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

    # Diatonic Modes (keeping these from before)
    @classmethod
    def Ionian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 9, 11], position)

    @classmethod
    def Dorian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 9, 10], position)

    @classmethod
    def Phrygian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 7, 8, 10], position)

    @classmethod
    def Lydian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 7, 9, 11], position)

    @classmethod
    def Mixolydian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 9, 10], position)

    @classmethod
    def Aeolian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 8, 10], position)

    @classmethod
    def Locrian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 6, 8, 10], position)

    # Additional Modes
    @classmethod
    def Ultralocrian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 4, 6, 8, 9], position)

    @classmethod
    def Superlocrian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 4, 6, 8, 10], position)

    # Melodic and Harmonic Minor Modes
    @classmethod
    def MelodicMinor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 9, 11], position)

    @classmethod
    def DorianFlat2(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 7, 9, 10], position)

    @classmethod
    def LydianAugmented(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 8, 9, 11], position)

    @classmethod
    def LydianDominant(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 7, 9, 10], position)

    @classmethod
    def MixolydianFlat6(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 8, 10], position)

    @classmethod
    def LocrianSharp2(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 6, 8, 10], position)

    @classmethod
    def AlteredDominant(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 4, 6, 8, 10], position)

    @classmethod
    def HarmonicMinor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 8, 11], position)

    @classmethod
    def LocrianNatural6(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 6, 9, 10], position)

    @classmethod
    def IonianSharp5(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 8, 9, 11], position)

    @classmethod
    def DorianSharp4(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 6, 7, 9, 10], position)

    @classmethod
    def PhrygianMajor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 7, 8, 10], position)

    @classmethod
    def LydianSharp2(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 3, 4, 6, 7, 9, 11], position)

    @classmethod
    def SuperlocrianDoubleFlat7(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 4, 6, 8, 9], position)

    # Pentatonic Scales
    @classmethod
    def MajorPentatonic(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 7, 9], position)

    @classmethod
    def MinorPentatonic(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 3, 5, 7, 10], position)

    @classmethod
    def EgyptianPentatonic(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 5, 7, 10], position)

    # Blues Scales
    @classmethod
    def BluesScale(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 3, 5, 6, 7, 10], position)

    @classmethod
    def MajorBluesScale(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 4, 7, 9], position)

    # Bebop Scales
    @classmethod
    def BebopDominant(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 9, 10, 11], position)

    @classmethod
    def BebopMajor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 8, 9, 11], position)

    @classmethod
    def BebopMinor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 4, 5, 7, 9, 10], position)

    @classmethod
    def BebopHarmonicMinor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 8, 9, 11], position)

    # Exotic Scales
    @classmethod
    def DoubleHarmonic(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 7, 8, 11], position)

    @classmethod
    def NeapolitanMinor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 7, 8, 11], position)

    @classmethod
    def NeapolitanMajor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 7, 9, 11], position)

    @classmethod
    def HungarianMinor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 6, 7, 8, 11], position)

    @classmethod
    def HungarianMajor(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 3, 4, 6, 7, 9, 10], position)

    @classmethod
    def Enigmatic(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 6, 8, 10, 11], position)

    @classmethod
    def PersianScale(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 6, 8, 11], position)

    @classmethod
    def ArabicScale(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 7, 8, 11], position)

    @classmethod
    def TodiTheta(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 6, 7, 8, 11], position)

    @classmethod
    def WholeTone(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 8, 10], position)

    @classmethod
    def Diminished(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 6, 8, 9, 11], position)

    @classmethod
    def DominantDiminished(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 4, 6, 7, 9, 10], position)

    @classmethod
    def Chromatic(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], position)

    # World Music Scales
    @classmethod
    def Algerian(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 6, 7, 8, 11], position)

    @classmethod
    def AugmentedScale(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 3, 4, 7, 8, 11], position)

    @classmethod
    def Balinese(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 7, 8], position)

    @classmethod
    def Byzantine(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 7, 8, 11], position)

    @classmethod
    def Chinese(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 7, 9], position)

    @classmethod
    def Hirajoshi(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 7, 8], position)

    @classmethod
    def InSen(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 5, 7, 10], position)

    @classmethod
    def Iwato(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 5, 6, 10], position)

    @classmethod
    def Kumoi(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 7, 9], position)

    @classmethod
    def Pelog(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 3, 7, 8], position)

    @classmethod
    def Prometheus(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 9, 10], position)

    @classmethod
    def SixToneSymmetrical(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 8, 9], position)

    @classmethod
    def Yo(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 5, 7, 9], position)

    # Additional World and Theoretical Scales
    @classmethod
    def Akebono(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 7, 9], position)

    @classmethod
    def Asavari(cls, scale_root, position=None):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 8, 10], position)