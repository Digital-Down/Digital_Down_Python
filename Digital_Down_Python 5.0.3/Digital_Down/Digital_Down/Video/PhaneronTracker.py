import pygame
import cv2
import mido
import os
import numpy as np
import bisect
from typing import Tuple, List, Dict

class PhaneronTracker:
    def __init__(self):
        # Initialize rendering settings
        self.fps = 30
        self.screen_width = 1920
        self.screen_height = 1080
        self.header_height = 108
        
        # Define colors
        self.active_color = (255, 255, 255)
        self.inactive_color = (0, 128, 0)
        self.inactive_line_color = (0, 128, 0)
        self.background_color = (0, 0, 0)
        self.bar_line_color = (0, 128, 0)
        
        # Track name mappings (can be customized later)
        self.track_name_mappings = {
            "bass": "Bass",
        }

        # Create a content box below header
        self.content_box = pygame.Rect(
            40,
            self.header_height + 20,
            self.screen_width - 80,
            self.screen_height - self.header_height - 40
        )
        
        # Actual content area (staff area) inside the content box
        self.content_area = pygame.Rect(
            self.content_box.left + 20,
            self.content_box.top + 20,
            self.content_box.width - 40,
            self.content_box.height - 40
        )
        
        # Initialize Pygame
        pygame.init()
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        self.screen = pygame.Surface((self.screen_width, self.screen_height))
        
        # Initialize fonts
        pygame.font.init()
        self.title_font = pygame.font.Font(None, 96)
        self.header_font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 24)
        self.musical_font = pygame.font.Font(None, 36)

        # Define drum note mappings
        self.drum_note_mappings = {
            35: "K",  # Kick 1 (C2)
            36: "K",  # Kick 1 (C2)
            37: "P1",  # Kick 1 (C2)
            38: "S",  # Snare 1 (D2)
            39: "Rim",  # Snare 1 (D2)
            50: "P1",  # Hi-Hat 1 (E-3)
            51: "P2",  # Hi-Hat 1 (E-3)
            42: "HH",  # Hi-Hat closed (F#2)
            43: "P8",  # Tom 2 (G2)
            49: "P3",  # Crash 1 (C#3)
            46: "P5", # Open Hi-Hat (B-2)
            44: "P4",  # Hi-Hat foot (G#2)
            41: "P9",  # Low tom (F2)
            47: "P6",  # Low tom (F2)
            45: "P7",  # Low tom (F2)
            55: "MLT",  # Low tom (F2)
            52: "LT",  # Low tom (F2)
            # Add more mappings as needed
        }
        
        # Define drum note mappings
        self.drum_note_mappings2 = {
            35: "K2",  # Kick 1 (C2)
            36: "K1",  # Kick 1 (C2)
            37: "Rim",  # Kick 1 (C2)
            38: "S1",  # Snare 1 (D2)
            39: "S2",  # Hi-Hat 1 (E2)
            41: "LT",  # Hi-Hat 1 (E2)
            40: "S3",  # Hi-Hat 1 (E2)
            42: "HH1",  # Hi-Hat closed (F#2)
            43: "MLT",  # Hi-Hat closed (F#2)
            44: "HH2",  # Hi-Hat closed (F#2)
            45: "MT",  # Crash 1 (C#3)
            46: "OH",  # Hi-Hat closed (F#2)
            43: "T2",  # Tom 2 (G2)
            47: "MHT",  # Crash 1 (C#3)
            48: "HT",  # Crash 1 (C#3)
            49: "C1",  # Crash 1 (C#3)
            50: "C2",  # Crash 1 (C#3)
            46: "OH",  # Open Hi-Hat (B-2)
            51: "R1",  # Hi-Hat 1 (E-3)
            52: "R2",  # Hi-Hat 1 (E-3)
            59: "P",  # Hi-Hat 1 (E-3)
            # Add more mappings as needed
        }

        # Define drum note mappings
        self.drum_note_mappings3 = {
            35: "K2",  # Kick 1 (C2)
            36: "K",  # Kick 1 (C2)
            37: "Rim",  # Kick 1 (C2)
            38: "S",  # Snare 1 (D2)
            40: "H1",  # Hi-Hat 1 (E2)
            42: "HH",  # Hi-Hat closed (F#2)
            43: "LT",  # Tom 2 (G2)
            45: "MT",  # Tom 2 (G2)
            46: "OH",  # Crash 1 (C#3)
            48: "HT",  # Crash 1 (C#3)
            49: "C",  # Crash 1 (C#3)
            51: "R",  # Crash 1 (C#3)
            46: "OH",  # Open Hi-Hat (B-2)
            # Add more mappings as needed
        }
        
        # MIDI note number to note name mapping
        self.note_names = {
            24: "C1", 25: "C#1", 26: "D1", 27: "D#1", 28: "E1", 29: "F1", 30: "F#1", 31: "G1",
            32: "G#1", 33: "A1", 34: "A#1", 35: "B1", 36: "C2", 37: "C#2", 38: "D2", 39: "D#2",
            40: "E2", 41: "F2", 42: "F#2", 43: "G2", 44: "G#2", 45: "A2", 46: "A#2", 47: "B2",
            48: "C3", 49: "C#3", 50: "D3", 51: "D#3", 52: "E3", 53: "F3", 54: "F#3", 55: "G3",
            56: "G#3", 57: "A3", 58: "A#3", 59: "B3", 60: "C4", 61: "C#4", 62: "D4", 63: "D#4",
            64: "E4", 65: "F4", 66: "F#4", 67: "G4", 68: "G#4", 69: "A4", 70: "A#4", 71: "B4",
            72: "C5", 73: "C#5", 74: "D5", 75: "D#5", 76: "E5", 77: "F5", 78: "F#5", 79: "G5",
            80: "G#5", 81: "A5", 82: "A#5", 83: "B5", 84: "C6", 85: "C#6", 86: "D6", 87: "D#6",
            88: "E6", 89: "F6", 90: "F#6", 91: "G6", 92: "G#6", 93: "A6", 94: "A#6", 95: "B6",
            96: "C7", 97: "C#7", 98: "D7", 99: "D#7", 100: "E7", 101: "F7", 102: "F#7", 103: "G7",
            104: "G#7", 105: "A7", 106: "A#7", 107: "B7"
        }

    def draw_header(self, title: str, scale: str, bpm: int):
        """Draw the header box with all specified text elements"""
        # Draw header background
        header_rect = pygame.Rect(
            self.content_box.left,  # x position (same as outermost tracker box)
            20,  # y position (moved down by 20 pixels)
            self.content_box.width,  # width (same as outermost tracker box)
            self.header_height - 20  # height (reduced by 20 pixels)
        )
        pygame.draw.rect(self.screen, self.background_color, header_rect)
        pygame.draw.rect(self.screen, self.inactive_line_color, header_rect, 2)
        
        # Calculate evenly spaced y positions for left and right text elements
        num_elements = 2  # Artist/Album on the left, Scale/BPM on the right
        spacing = header_rect.height // (num_elements + 1)  # Divide height into equal parts
        
        # Left side information (Artist and Album)
        artist_text = self.header_font.render("Artist: Digital Down", True, self.active_color)
        album_text = self.header_font.render("Album: Mutagen Eve", True, self.active_color)
        
        # Position artist and album text (left side, evenly spaced)
        self.screen.blit(artist_text, (header_rect.left + 20, header_rect.top + 10))  # First spacing
        self.screen.blit(album_text, (header_rect.left + 20, header_rect.bottom - 40))  # Second spacing
        
        # Right side information (Scale and BPM)
        scale_text = self.header_font.render(f"Scale: {scale}", True, self.active_color)
        bpm_text = self.header_font.render(f"BPM: {bpm}", True, self.active_color)
        
        # Position scale and BPM text (right side, evenly spaced)
        scale_x = header_rect.right - scale_text.get_width() - 20  # Right edge with margin
        bpm_x = header_rect.right - bpm_text.get_width() - 20  # Right edge with margin
        
        self.screen.blit(scale_text, (scale_x, header_rect.top + 10))  # First spacing
        self.screen.blit(bpm_text, (bpm_x, header_rect.bottom - 40))  # Second spacing
        
        # Center title text vertically and horizontally
        title_text = self.title_font.render(title, True, self.active_color)
        title_x = (self.screen_width - title_text.get_width()) // 2  # Center horizontally
        title_y = header_rect.centery - title_text.get_height() // 2 + 2  # Center vertically
        self.screen.blit(title_text, (title_x, title_y))

    def get_note_name(self, note_num, track_name: str):
        """Get note name based on MIDI note number and apply drum mappings if necessary"""
        # Check if the track is a drum track
        if track_name in ["Drumkit 1"]:
            # Apply drum note mappings
            return self.drum_note_mappings.get(note_num, self.note_names.get(note_num, f"Note{note_num}"))
        
        # Check if the track is another drum track
        if track_name in ["Drumkit 2"]:
            # Apply drum note mappings
            return self.drum_note_mappings2.get(note_num, self.note_names.get(note_num, f"Note{note_num}"))
        
        # Check if the track is another drum track
        if track_name in ["Drumkit 3"]:
            # Apply drum note mappings
            return self.drum_note_mappings2.get(note_num, self.note_names.get(note_num, f"Note{note_num}"))


        # Default to standard note names
        return self.note_names.get(note_num, f"Note{note_num}")

    def calculate_rows_for_time_signature(self, numerator: int, denominator: int) -> int:
        """Calculate how many 32nd note rows to display for a given time signature"""
        # Base calculation for 4/4 time: 32 rows
        base_rows = 32  # This represents 4/4 time (4 quarter notes)
        return int(numerator * (32 / denominator))

    def process_midi_file(self, midi_file: str, ppq_override: int = None) -> Dict:
        """Process MIDI file using mido and return note data organized by track"""
        mid = mido.MidiFile(midi_file)
        ppq = ppq_override or mid.ticks_per_beat
        
        # Collect time signatures, tempo changes, and max_tick
        time_signatures = []
        tempo_changes = []
        max_tick = 0
        
        for track in mid.tracks:
            track_time = 0
            for msg in track:
                track_time += msg.time
                if msg.type == 'time_signature':
                    time_signatures.append({
                        'tick': track_time,
                        'numerator': msg.numerator,
                        'denominator': msg.denominator,
                        'bar': int(track_time / (ppq * 4))
                    })
                elif msg.type == 'set_tempo':
                    tempo_changes.append({
                        'tick': track_time,
                        'tempo': msg.tempo
                    })
            if track_time > max_tick:
                max_tick = track_time

        # Handle time signatures
        time_signatures.sort(key=lambda x: x['tick'])
        if not time_signatures:
            time_signatures.append({
                'tick': 0,
                'numerator': 4,
                'denominator': 4,
                'bar': 0
            })

        # Calculate bar data
        bar_data = {}
        current_sig = time_signatures[0]
        sig_index = 1
        approximate_bars = int(max_tick / (ppq * 4)) + 1
        
        for bar in range(approximate_bars):
            if sig_index < len(time_signatures) and bar >= time_signatures[sig_index]['bar']:
                current_sig = time_signatures[sig_index]
                sig_index += 1
            
            rows_in_bar = self.calculate_rows_for_time_signature(
                current_sig['numerator'], 
                current_sig['denominator']
            )
            bar_data[bar] = {
                'rows': rows_in_bar,
                'numerator': current_sig['numerator'],
                'denominator': current_sig['denominator']
            }

        # Process tempo changes
        tempo_changes.sort(key=lambda x: x['tick'])
        if not tempo_changes:
            tempo_changes.append({'tick': 0, 'tempo': 500000})

        # Create tempo segments
        tempo_segments = []
        current_tick = 0
        current_time = 0.0
        current_tempo = tempo_changes[0]['tempo']
        ppq_used = ppq

        for tc in tempo_changes:
            if current_tick < tc['tick']:
                delta_ticks = tc['tick'] - current_tick
                delta_time = delta_ticks * (current_tempo / ppq_used) / 1e6
                tempo_segments.append({
                    'start_tick': current_tick,
                    'end_tick': tc['tick'],
                    'tempo': current_tempo,
                    'start_time': current_time,
                    'end_time': current_time + delta_time
                })
                current_time += delta_time
            current_tick = tc['tick']
            current_tempo = tc['tempo']

        if current_tick < max_tick:
            delta_ticks = max_tick - current_tick
            delta_time = delta_ticks * (current_tempo / ppq_used) / 1e6
            tempo_segments.append({
                'start_tick': current_tick,
                'end_tick': max_tick,
                'tempo': current_tempo,
                'start_time': current_time,
                'end_time': current_time + delta_time
            })
            current_time += delta_time

        # Calculate row times
        ticks_per_row = ppq_used / 8
        total_rows = int(max_tick / ticks_per_row) + 1
        row_times = []

        for row in range(total_rows):
            row_tick = row * ticks_per_row
            for segment in tempo_segments:
                if segment['start_tick'] <= row_tick < segment['end_tick']:
                    delta = row_tick - segment['start_tick']
                    time_in_seg = delta * (segment['tempo'] / ppq_used) / 1e6
                    row_times.append(segment['start_time'] + time_in_seg)
                    break
            else:
                last_seg = tempo_segments[-1]
                delta = row_tick - last_seg['start_tick']
                time_in_seg = delta * (last_seg['tempo'] / ppq_used) / 1e6
                row_times.append(last_seg['start_time'] + time_in_seg)

        # Create bar-row mapping
        bar_row_map = []
        sorted_bars = sorted(bar_data.keys())
        current_global_row = 0
        for bar in sorted_bars:
            rows_in_bar = bar_data[bar]['rows']
            for r in range(rows_in_bar):
                bar_row_map.append((bar, r))
            current_global_row += rows_in_bar

        # Process tracks
        tracks_data = {}
        for track_idx, track in enumerate(mid.tracks):
            # Track has notes?
            has_notes = False
            for msg in track:
                if msg.type in ('note_on', 'note_off'):
                    has_notes = True
                    break
            
            if not has_notes:
                continue  # Skip tracks with no notes (like metadata tracks)
            
            # Get track name
            track_name = f"Track {track_idx + 1}"
            for msg in track:
                if msg.type == 'track_name' and msg.name:
                    track_name = msg.name
                    break
            
            # Apply track name mapping
            display_name = self.track_name_mappings.get(track_name, track_name)
            tracks_data[display_name] = []
            
            # Track absolute time for this track
            track_time = 0
            active_notes = {}  # note_number -> start_time
            
            # Process messages
            for msg in track:
                track_time += msg.time
                
                if msg.type == 'note_on' and msg.velocity > 0:
                    # Note start
                    active_notes[msg.note] = track_time
                
                elif (msg.type == 'note_off') or (msg.type == 'note_on' and msg.velocity == 0):
                    # Note end (note_off or note_on with velocity 0)
                    if msg.note in active_notes:
                        start_time = active_notes[msg.note]
                        duration = track_time - start_time
                        
                        # Convert to 32nd note positions
                        start_32nd = int(start_time / ticks_per_row)
                        duration_32nd = max(1, int(duration / ticks_per_row))  # Min duration 1
                        
                        note_name = self.get_note_name(msg.note, display_name)
                        
                        tracks_data[display_name].append({
                            'start': start_32nd,
                            'duration': duration_32nd,
                            'note': note_name
                        })
                        
                        # Remove from active notes
                        del active_notes[msg.note]
        
        return {
            'tracks': tracks_data,
            'bars': bar_data,
            'row_times': row_times,
            'bar_row_map': bar_row_map,
            'tempo_segments': tempo_segments
        }

    def draw_tracker_grid(self, data_dict: Dict, current_row: int, current_bar: int):
        """Draw the tracker-style grid with notes, adapting to the time signature of the current bar"""
        tracks_data = data_dict['tracks']
        bar_data = data_dict['bars']
        
        # Get current bar info
        current_bar_info = bar_data.get(current_bar, {'rows': 32, 'numerator': 4, 'denominator': 4})
        rows_to_display = current_bar_info['rows']
        
        num_tracks = len(tracks_data)
        track_width = (self.content_area.width - 2) // num_tracks
        row_height = (self.content_area.height - 2) // 32  # Keep row height constant

        # Draw the outer green box - ADJUSTED TO ONLY SPAN THE NEEDED ROWS
        adjusted_content_box = pygame.Rect(
            self.content_box.left,
            self.content_box.top,
            self.content_box.width,
            row_height * (rows_to_display + 1) + 40  # +1 for header row, +40 for padding
        )
        pygame.draw.rect(self.screen, (0, 128, 0), adjusted_content_box, 2)
        
        # Draw track names with green boxes that span the full track width
        x = self.content_area.left
        for track_name in tracks_data.keys():
            track_name_text = self.small_font.render(track_name, True, (255, 255, 255))  # White text
            text_rect = track_name_text.get_rect(center=(x + track_width // 2, 
                                                  self.content_area.top + row_height // 2))  # Center vertically
            
            # Draw the green box spanning the full track width
            box_rect = pygame.Rect(
                x,  # Start at the left edge of the track
                self.content_area.top,  # Align with the top of the content area
                track_width,  # Span the full track width
                row_height  # Match the height of a row
            )
            pygame.draw.rect(self.screen, (0, 128, 0), box_rect)  # Fill with green
            pygame.draw.rect(self.screen, (0, 0, 0), box_rect, 1)  # Black border
            
            # Draw the track name text centered within the green box
            self.screen.blit(track_name_text, text_rect)
            
            x += track_width

        # Draw grid and notes for each track
        for track_idx, (track_name, notes) in enumerate(tracks_data.items()):
            track_x = self.content_area.left + (track_idx * track_width)
            
            # Draw vertical track separator ONLY up to the last visible row
            pygame.draw.line(self.screen, self.inactive_line_color,
                             (track_x, self.content_area.top + row_height),  # Move down by one row
                             (track_x, self.content_area.top + (rows_to_display + 1) * row_height))  # Visible rows + track name row
            
            # Create note grid for this bar only
            note_grid = [[] for _ in range(rows_to_display)]
            
            # Calculate the start and end offsets for the current bar
            # For variable time signatures, we need to calculate the cumulative 32nd notes before this bar
            cumulative_rows = 0
            for i in range(current_bar):
                cumulative_rows += bar_data.get(i, {'rows': 32})['rows']
            
            bar_start = cumulative_rows
            bar_end = bar_start + rows_to_display
            
            # Fixed part: Handle notes crossing bar boundaries
            for note in notes:
                note_start = note['start']
                note_duration = note['duration']
                note_end = note_start + note_duration
                note_name = note['note']
                
                # If the note overlaps with the current bar
                if (bar_start <= note_start < bar_end) or (note_start < bar_start and note_end > bar_start):
                    # Calculate the position within this bar where the note starts
                    if note_start < bar_start:
                        # Note started in a previous bar
                        remaining_duration = note_end - bar_start
                        relative_start = 0
                    else:
                        # Note starts in this bar
                        remaining_duration = note_end - note_start
                        relative_start = note_start - bar_start
                    
                    # Ensure we only show the portion of the note that's in this bar
                    duration_in_this_bar = min(remaining_duration, rows_to_display - relative_start)
                    
                    if duration_in_this_bar > 0 and relative_start < rows_to_display:
                        # Add the note name at the starting position (or continuation marker if from previous bar)
                        if note_start < bar_start:
                            # This is a continuation from previous bar, so use '-'
                            note_grid[relative_start].append('-')
                        else:
                            # This note starts in this bar, so use the note name
                            note_grid[relative_start].append(note_name)
                        
                        # Add continuation markers for the rest of the duration within this bar
                        for i in range(1, duration_in_this_bar):
                            if relative_start + i < rows_to_display:  # Stay within bar boundary
                                if note_name not in note_grid[relative_start + i]:
                                    note_grid[relative_start + i].append('-')
            
            # Draw each cell in the track for ONLY the rows_to_display
            for row in range(rows_to_display):
                y = self.content_area.top + (row * row_height) + row_height  # Move down by one row
                cell_rect = pygame.Rect(track_x, y, track_width, row_height)
                
                has_note = len(note_grid[row]) > 0
                is_current_or_previous_row = row <= current_row  # Check if row is active or has been active
                
                # Set cell colors based on state
                if has_note:
                    if is_current_or_previous_row:
                        # Active or previously active note - green background with black text
                        pygame.draw.rect(self.screen, self.inactive_line_color, cell_rect)
                        text_color = (0, 0, 0)
                    else:
                        # Upcoming note - black background with green text
                        pygame.draw.rect(self.screen, self.background_color, cell_rect)
                        text_color = self.inactive_line_color
                else:
                    if is_current_or_previous_row:
                        # Active or previously active empty cell - white background
                        pygame.draw.rect(self.screen, self.active_color, cell_rect)
                    else:
                        # Empty cell - black background
                        pygame.draw.rect(self.screen, self.background_color, cell_rect)
                
                # Determine border color based on whether the row is active or has been active
                border_color = (0, 0, 0) if is_current_or_previous_row else self.inactive_line_color
                pygame.draw.rect(self.screen, border_color, cell_rect, 1)
                
                # Handle multiple notes in the same row
                if note_grid[row]:
                    num_notes = len(note_grid[row])
                    section_width_base = track_width // num_notes
                    remainder = track_width % num_notes
                    current_x = track_x

                    for i, note_text in enumerate(note_grid[row]):
                        # Calculate section width with remainder distribution
                        if i < remainder:
                            section_width = section_width_base + 1
                        else:
                            section_width = section_width_base

                        section_rect = pygame.Rect(
                            current_x,
                            y,
                            section_width,
                            row_height
                        )
                        
                        # Draw section background
                        if is_current_or_previous_row:
                            pygame.draw.rect(self.screen, self.inactive_line_color, section_rect)
                        else:
                            pygame.draw.rect(self.screen, self.background_color, section_rect)
                        
                        # Draw section border
                        pygame.draw.rect(self.screen, border_color, section_rect, 1)
                        
                        # Render note text
                        if note_text != '-':
                            note_render = self.small_font.render(note_text, True, text_color)
                            text_rect = note_render.get_rect(center=section_rect.center)
                            self.screen.blit(note_render, text_rect)
                        else:
                            # Render '-' symbol for held notes
                            dash_render = self.small_font.render('-', True, text_color)
                            text_rect = dash_render.get_rect(center=section_rect.center)
                            self.screen.blit(dash_render, text_rect)

                        current_x += section_width

    def render_to_video(self, midi_file: str, output_file: str, bpm: int, duration: float, ppq_override: int = None):
        """Render the tracker animation to a video file"""
        # Set up video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        total_frames = int(duration * self.fps)
        video = cv2.VideoWriter(output_file, fourcc, self.fps, 
                              (self.screen_width, self.screen_height))

        # Process MIDI data once - now returns both tracks and bar data
        data_dict = self.process_midi_file(midi_file, ppq_override)
        row_times = data_dict['row_times']
        bar_row_map = data_dict['bar_row_map']
        tempo_segments = data_dict['tempo_segments']
        bar_data = data_dict['bars']

        for frame in range(total_frames):
            current_time = frame / self.fps
            global_row = bisect.bisect_right(row_times, current_time) - 1
            if global_row < 0:
                global_row = 0

            if global_row >= len(bar_row_map):
                current_bar = max(bar_data.keys())
                current_row_in_bar = bar_data[current_bar]['rows'] - 1
            else:
                current_bar, current_row_in_bar = bar_row_map[global_row]

            # Calculate current BPM
            current_bpm = 120
            for seg in tempo_segments:
                if seg['start_time'] <= current_time < seg['end_time']:
                    current_bpm = 60000000 / seg['tempo']
                    break
            else:
                current_bpm = 60000000 / tempo_segments[-1]['tempo']

            self.screen.fill(self.background_color)
            current_bar_info = bar_data.get(current_bar, {'numerator':4, 'denominator':4})
            time_sig = f"{current_bar_info['numerator']}/{current_bar_info['denominator']}"
            
            self.draw_header("Title", "C Minor", int(round(current_bpm)))
            self.draw_tracker_grid(data_dict, current_row_in_bar, current_bar)

            frame_data = pygame.surfarray.array3d(self.screen)
            frame_data = frame_data.transpose([1, 0, 2])
            frame_data = cv2.cvtColor(frame_data, cv2.COLOR_RGB2BGR)
            video.write(frame_data)

            if frame % 30 == 0:
                print(f"Rendering frame {frame}/{total_frames} (Bar {current_bar + 1}, Row {current_row_in_bar + 1})")

        video.release()
        print(f"Video saved to {output_file}")

#midi_file = "test.mid"
#output_file = "test.mp4"
#bpm = 120
#duration = 120

#PhaneronTracker.render_to_video(midi_file, output_file, bpm, duration)