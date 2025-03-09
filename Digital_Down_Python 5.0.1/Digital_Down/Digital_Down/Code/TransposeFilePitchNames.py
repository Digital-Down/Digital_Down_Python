import os
import re

class TransposeFilePitchNames:
    # Class variable accessible to all class methods
    _notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    @classmethod
    def _transpose_single_note(cls, note_str, semitones):
        """
        Transpose a single note name by given number of semitones.
        Example: ('B6', -4) -> 'A5'
        """
        # Extract note and octave using regex
        match = re.match(r'([A-G]#?)(\d+)', note_str)
        if not match:
            return note_str
            
        note, octave = match.groups()
        octave = int(octave)
        
        # Find current note index
        current_index = cls._notes.index(note)
        
        # Calculate new note index and octave
        new_index = (current_index + semitones) % 12
        octave_change = (current_index + semitones) // 12
        new_octave = octave + octave_change
        
        return f"{cls._notes[new_index]}{new_octave}"
    
    @classmethod
    def _process_filename(cls, filename, semitones):
        """
        Process a single filename, transposing the note if found.
        Example: 'B6 MS2.wav' -> 'A5 MS2.wav'
        """
        # Match note pattern at start of filename
        match = re.match(r'([A-G]#?\d+)(.*)', filename)
        if not match:
            return filename
            
        note_part, rest = match.groups()
        new_note = cls._transpose_single_note(note_part, semitones)
        return f"{new_note}{rest}"
    
    @classmethod
    def batch_transpose(cls, folder_path, semitones):
        """
        Recursively process all files in the given folder and its subfolders,
        renaming files in two phases to avoid conflicts.
        
        Phase 1: Add 'Renamed' suffix to all transposed files
        Phase 2: Remove 'Renamed' suffix from all files
        
        Args:
            folder_path (str): Path to the root folder
            semitones (int): Number of semitones to transpose (positive or negative)
        """
        # Phase 1: Rename all files with 'Renamed' suffix
        print("Phase 1: Adding temporary suffixes...")
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                if ' Renamed' not in filename:  # Skip already renamed files
                    new_filename = cls._process_filename(filename, semitones)
                    
                    if new_filename != filename:
                        # Add 'Renamed' suffix before the file extension
                        name, ext = os.path.splitext(new_filename)
                        temp_filename = f"{name} Renamed{ext}"
                        
                        old_path = os.path.join(root, filename)
                        new_path = os.path.join(root, temp_filename)
                        
                        try:
                            os.rename(old_path, new_path)
                            print(f"Phase 1: {filename} -> {temp_filename}")
                        except OSError as e:
                            print(f"Error renaming {filename}: {e}")

        # Phase 2: Remove 'Renamed' suffix from all files
        print("\nPhase 2: Removing temporary suffixes...")
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                if ' Renamed' in filename:  # Check for space before 'Renamed'
                    # Remove 'Renamed' suffix
                    name, ext = os.path.splitext(filename)
                    final_filename = name.replace(' Renamed', '') + ext
                    
                    old_path = os.path.join(root, filename)
                    new_path = os.path.join(root, final_filename)
                    
                    try:
                        os.rename(old_path, new_path)
                        print(f"Phase 2: {filename} -> {final_filename}")
                    except OSError as e:
                        print(f"Error renaming {filename}: {e}")
        
        print("\nTransposition complete!")