class Chords:
    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    @classmethod
    def _get_scale(cls, scale_root, intervals):
        if scale_root not in cls.NOTES:
            raise ValueError(f"Invalid root note. Please use one of: {', '.join(cls.NOTES)}")
        
        root_index = cls.NOTES.index(scale_root)
        scale = [cls.NOTES[(root_index + interval) % 12] for interval in intervals]
        return scale


    @classmethod
    def aug(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 8])
    @classmethod
    def aug11th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 7, 10])
    @classmethod
    def augmaj7th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 8, 11])
    @classmethod
    def aug7th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 8, 10])
    @classmethod
    def aug6thitalian(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 10])
    @classmethod
    def aug6thfrench(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 6, 10])
    @classmethod
    def aug6thgerman(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 7, 10])
    @classmethod
    def dim(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 6])
    @classmethod
    def dimmaj7th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 6, 10])
    @classmethod
    def dim7th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 6, 9])
    @classmethod
    def dom11th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 10])
    @classmethod
    def dommin9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 4, 7, 10])
    @classmethod
    def dom9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 7, 10])
    @classmethod
    def min(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 7])
    @classmethod
    def dom7thsharp9(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 4, 7, 10])
    @classmethod
    def dom13th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 9, 10])
    @classmethod
    def dream(cls, scale_root):
        return cls._get_scale(scale_root, [0, 5, 6, 7])
    @classmethod
    def elektra(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 4, 7, 9])
    @classmethod
    def farben(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 8, 9, 11])
    @classmethod
    def lydian(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 6, 7, 11])
    @classmethod
    def magic(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 3, 5, 6, 10])
    @classmethod
    def maj(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 7])
    @classmethod
    def maj11th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 11])
    @classmethod
    def maj7th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 7, 11])
    @classmethod
    def maj7thsharp11(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 6, 8, 11])
    @classmethod
    def maj6th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 7, 9])
    @classmethod
    def maj6th9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 7, 9])
    @classmethod
    def maj9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 7, 11])
    @classmethod
    def maj13th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 5, 7, 9, 11])
    @classmethod
    def min11th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 10])
    @classmethod
    def min7th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 7, 10])
    @classmethod
    def min9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 3, 7, 10])
    @classmethod
    def min6th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 7, 9])
    @classmethod
    def min6th9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 3, 7, 9])
    @classmethod
    def min13th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 3, 5, 7, 9, 10])
    @classmethod
    def mystic(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 6, 9, 10])
    @classmethod
    def neapolitan(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 5, 8])
    @classmethod
    def ninethaug5th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 2, 4, 7, 8, 10])
    @classmethod
    def northernlights(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 2, 3, 4, 6, 7, 8, 10, 11])
    @classmethod
    def hexa(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 4, 5, 8, 9])
    @classmethod
    def petrushka(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 4, 6, 7, 10])
    @classmethod
    def power(cls, scale_root):
        return cls._get_scale(scale_root, [0, 7])
    @classmethod
    def sevensix(cls, scale_root):
        return cls._get_scale(scale_root, [0, 4, 7, 9, 10])
    @classmethod
    def seventhsus4(cls, scale_root):
        return cls._get_scale(scale_root, [0, 5, 7, 10])
    @classmethod
    def sowhat(cls, scale_root):
        return cls._get_scale(scale_root, [0, 3, 5, 7, 10])
    @classmethod
    def thirteenthflat9th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 4, 7, 9, 10])
    @classmethod
    def thirteenthflat9thflat5th(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 4, 6, 9, 10])
    @classmethod
    def viennese1(cls, scale_root):
        return cls._get_scale(scale_root, [0, 1, 6])
    @classmethod
    def viennese2(cls, scale_root):
        return cls._get_scale(scale_root, [0, 6, 7])
