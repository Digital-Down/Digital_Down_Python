"""
__________________________________________________________________________________
#####################
#MindHarvestNetwork#
#####################

The original Mind Harvest Network animations.
(Place Wav file in folder alongside script)
__________________________________________________________________________________

###########
##Methods##
###########
1.horizontal		horizontal video 1920 x 1080
2.vertical			vertical video 1080 x 1920
__________________________________________________________________________________
####################
##Method Arguments##
####################
User Defined Arguments
1.(WAV File Name.wav)
__________________________________________________________________________________
"""
import numpy as np
import cv2
import wave
import os
from moviepy.editor import VideoFileClip, AudioFileClip

class MindHarvestNetwork:
    def __init__(self): 
        pass

    @classmethod
    def horizontal(cls, wav_file_path, output_folder):
        # Check if input file exists
        if not os.path.exists(wav_file_path):
            raise FileNotFoundError(f"The input file {wav_file_path} does not exist.")
        input_filename = os.path.basename(wav_file_path)
        output_filename = os.path.splitext(input_filename)[0] + '.mp4'
        output_video_path = os.path.join(output_folder, output_filename)

        # Parameters
        fps = 30
        resolution = (1920, 1080)
        box_width = 780
        left_box_x_start = 90
        right_box_x_start = resolution[0] - box_width - left_box_x_start
        buffer_y = 90
        node_radius = 20
        active_color = (255, 255, 255)  # White for active elements
        inactive_color = (0, 128, 0)  # Dark green for inactive circles
        inactive_line_color = (0, 255, 0)  # Bright green for inactive lines
        active_line_thickness = 2
        inactive_line_thickness = 1

        # Read the wave file
        with wave.open(wav_file_path, 'r') as wav:
            n_channels, sampwidth, framerate, n_frames, comptype, compname = wav.getparams()
            frames = wav.readframes(n_frames)
            samples = np.frombuffer(frames, dtype=np.int16)
            samples = samples.reshape(-1, n_channels)

        # Calculate number of samples per frame
        samples_per_frame = framerate // fps

        # Initialize video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        temp_video_path = os.path.join(output_folder, 'temp_output.mp4')
        video_writer = cv2.VideoWriter(temp_video_path, fourcc, fps, resolution)

        # Create buffer for right side pixels
        right_box_height = resolution[1] - 2 * buffer_y
        pixel_buffer = np.zeros((right_box_height, box_width, 3), dtype=np.uint8)

        # Function to draw inactive nodes with black inner circle
        def draw_inactive_node(frame, x, y, outer_radius, inner_radius, outer_color, inner_color):
            cv2.circle(frame, (x, y), outer_radius, outer_color, 2, lineType=cv2.LINE_AA)
            cv2.circle(frame, (x, y), inner_radius, inner_color, cv2.FILLED, lineType=cv2.LINE_AA)

        # Function to get node positions and active status
        def get_layer_nodes(layer, x, y_start, y_end, value):
            y_positions = np.linspace(y_start, y_end, len(layer))
            nodes = []
            for i in range(len(layer)):
                y = int(y_positions[i])
                is_active = layer[i] == value
                nodes.append((x, y, is_active))
            return nodes

        layers = [
            [value for value in range(7)],   # 10,000s place (0-6)
            [value for value in range(10)],  # 1,000s place (0-9)
            [value for value in range(10)],  # 100s place (0-9)
            [value for value in range(10)],  # 10s place (0-9)
            [value for value in range(10)]   # 1s place (0-9)
        ]

        # Generate frames
        for frame_idx in range(len(samples) // samples_per_frame):
            frame = np.zeros((resolution[1], resolution[0], 3), dtype=np.uint8)
            
            # Draw Mind Harvest Network text (centered)
            text = 'Mind Harvest Network'
            text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
            text_x = (resolution[0] - text_size[0]) // 2
            cv2.putText(frame, text, (text_x, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, lineType=cv2.LINE_AA)
            
            # Draw equal sign
            cv2.putText(frame, '=', (910, resolution[1] // 2), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4, lineType=cv2.LINE_AA)

            # Process current frame samples
            frame_samples = samples[frame_idx * samples_per_frame:(frame_idx + 1) * samples_per_frame]
            avg_sample = int(np.mean(np.abs(frame_samples)))

            # Get node positions for each digit place
            digits = [
                (avg_sample // 10000) % 10,
                (avg_sample // 1000) % 10,
                (avg_sample // 100) % 10,
                (avg_sample // 10) % 10,
                avg_sample % 10
            ]
            x_positions = np.linspace(left_box_x_start + 50, left_box_x_start + box_width - 50, len(layers)).astype(int)
            y_start = buffer_y + 50
            y_end = resolution[1] - buffer_y - 50

            node_positions = []
            for layer, digit, x in zip(layers, digits, x_positions):
                nodes = get_layer_nodes(layer, x, y_start, y_end, digit)
                node_positions.append(nodes)

            # Draw connecting lines
            for i in range(len(node_positions) - 1):
                # First, draw all inactive lines
                for start_node in node_positions[i]:
                    for end_node in node_positions[i + 1]:
                        if not (start_node[2] and end_node[2]):
                            cv2.line(frame, start_node[:2], end_node[:2], inactive_line_color, inactive_line_thickness, lineType=cv2.LINE_AA)
                
                # Then, draw all active lines
                for start_node in node_positions[i]:
                    for end_node in node_positions[i + 1]:
                        if start_node[2] and end_node[2]:
                            cv2.line(frame, start_node[:2], end_node[:2], active_color, active_line_thickness, lineType=cv2.LINE_AA)

            # Draw nodes
            for layer_nodes in node_positions:
                for x, y, is_active in layer_nodes:
                    if is_active:
                        cv2.circle(frame, (x, y), node_radius, active_color, cv2.FILLED, lineType=cv2.LINE_AA)
                    else:
                        draw_inactive_node(frame, x, y, node_radius, node_radius - 2, inactive_color, (0, 0, 0))

            # Draw right side box
            cv2.rectangle(frame, (right_box_x_start, buffer_y), (right_box_x_start + box_width, resolution[1] - buffer_y), (255, 255, 255), 2, lineType=cv2.LINE_AA)

            # Calculate averages for this frame
            hist, _ = np.histogram(np.abs(frame_samples), bins=right_box_height, range=(0, 2**15))
            y_values = hist / np.max(hist) * 255  # Scale to 0-255 for intensity

            # Shift pixel buffer to the left
            pixel_buffer[:, :-1] = pixel_buffer[:, 1:]

            # Add new values to the right side of the buffer
            for y in range(right_box_height):
                pixel_buffer[y, -1] = (0, int(y_values[y]), 0)  # Green channel based on y_values

            # Draw pixel buffer in the right box
            frame[buffer_y:buffer_y + right_box_height, right_box_x_start:right_box_x_start + box_width] = pixel_buffer
            
            # Write frame to video
            video_writer.write(frame)

        # Release video writer
        video_writer.release()

        # Add audio to the video
        cls.add_audio_to_video(wav_file_path, temp_video_path, output_video_path)

        # Remove temporary video file
        os.remove(temp_video_path)

    @classmethod
    def vertical(cls, wav_file_path, output_folder):
        input_filename = os.path.basename(wav_file_path)
        output_filename = os.path.splitext(input_filename)[0] + '.mp4'
        output_video_path = os.path.join(output_folder, output_filename)
        # Check if input file exists
        if not os.path.exists(wav_file_path):
            raise FileNotFoundError(f"The input file {wav_file_path} does not exist.")

        # Parameters
        fps = 30
        resolution = (1080, 1920)  # Swapped for vertical video
        box_width = 900
        left_box_x_start = 90
        buffer_y = 90
        node_radius = 20
        active_color = (255, 255, 255)  # White for active elements
        inactive_color = (0, 128, 0)  # Dark green for inactive circles
        inactive_line_color = (0, 255, 0)  # Bright green for inactive lines
        active_line_thickness = 2
        inactive_line_thickness = 1

        # Read the wave file
        with wave.open(wav_file_path, 'r') as wav:
            n_channels, sampwidth, framerate, n_frames, comptype, compname = wav.getparams()
            frames = wav.readframes(n_frames)
            samples = np.frombuffer(frames, dtype=np.int16)
            samples = samples.reshape(-1, n_channels)

        # Calculate number of samples per frame
        samples_per_frame = framerate // fps

        # Initialize video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        temp_video_path = os.path.join(output_folder, 'temp_output.mp4')
        video_writer = cv2.VideoWriter(temp_video_path, fourcc, fps, resolution)

        # Create buffer for bottom histogram
        histogram_height = 600
        pixel_buffer = np.zeros((histogram_height, box_width, 3), dtype=np.uint8)

        # Function to draw inactive nodes with black inner circle
        def draw_inactive_node(frame, x, y, outer_radius, inner_radius, outer_color, inner_color):
            cv2.circle(frame, (x, y), outer_radius, outer_color, 2, lineType=cv2.LINE_AA)
            cv2.circle(frame, (x, y), inner_radius, inner_color, cv2.FILLED, lineType=cv2.LINE_AA)

        # Function to get node positions and active status
        def get_layer_nodes(layer, x, y_start, y_end, value):
            y_positions = np.linspace(y_start, y_end, len(layer))
            nodes = []
            for i in range(len(layer)):
                y = int(y_positions[i])
                is_active = layer[i] == value
                nodes.append((x, y, is_active))
            return nodes

        layers = [
            [value for value in range(7)],   # 10,000s place (0-6)
            [value for value in range(10)],  # 1,000s place (0-9)
            [value for value in range(10)],  # 100s place (0-9)
            [value for value in range(10)],  # 10s place (0-9)
            [value for value in range(10)]   # 1s place (0-9)
        ]

        # Generate frames
        for frame_idx in range(len(samples) // samples_per_frame):
            frame = np.zeros((resolution[1], resolution[0], 3), dtype=np.uint8)
            
            # Process current frame samples
            frame_samples = samples[frame_idx * samples_per_frame:(frame_idx + 1) * samples_per_frame]
            avg_sample = int(np.mean(np.abs(frame_samples)))

            # Get node positions for each digit place
            digits = [
                (avg_sample // 10000) % 10,
                (avg_sample // 1000) % 10,
                (avg_sample // 100) % 10,
                (avg_sample // 10) % 10,
                avg_sample % 10
            ]
            x_positions = np.linspace(left_box_x_start, resolution[0] - left_box_x_start, len(layers)).astype(int)
            y_start = buffer_y + 200  # Adjusted to leave space for title
            y_end = resolution[1] - buffer_y - histogram_height - 100  # Adjusted to leave more space at the bottom

            node_positions = []
            for layer, digit, x in zip(layers, digits, x_positions):
                nodes = get_layer_nodes(layer, x, y_start, y_end, digit)
                node_positions.append(nodes)

            # Draw Mind Harvest Network text (centered between top and nodes)
            text = 'Mind Harvest Network'
            text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
            text_x = (resolution[0] - text_size[0]) // 2
            text_y = (y_start + buffer_y) // 2
            cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, lineType=cv2.LINE_AA)

            # Draw connecting lines
            for i in range(len(node_positions) - 1):
                # First, draw all inactive lines
                for start_node in node_positions[i]:
                    for end_node in node_positions[i + 1]:
                        if not (start_node[2] and end_node[2]):
                            cv2.line(frame, start_node[:2], end_node[:2], inactive_line_color, inactive_line_thickness, lineType=cv2.LINE_AA)
                
                # Then, draw all active lines
                for start_node in node_positions[i]:
                    for end_node in node_positions[i + 1]:
                        if start_node[2] and end_node[2]:
                            cv2.line(frame, start_node[:2], end_node[:2], active_color, active_line_thickness, lineType=cv2.LINE_AA)

            # Draw nodes
            for layer_nodes in node_positions:
                for x, y, is_active in layer_nodes:
                    if is_active:
                        cv2.circle(frame, (x, y), node_radius, active_color, cv2.FILLED, lineType=cv2.LINE_AA)
                    else:
                        draw_inactive_node(frame, x, y, node_radius, node_radius - 2, inactive_color, (0, 0, 0))

			# Draw equal sign (centered between nodes and histogram)
            histogram_start_y = resolution[1] - histogram_height - buffer_y
            equal_y = (y_end + histogram_start_y) // 2
            cv2.putText(frame, '=', (resolution[0] // 2, equal_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4, lineType=cv2.LINE_AA)

            # Calculate averages for this frame
            hist, _ = np.histogram(np.abs(frame_samples), bins=box_width, range=(0, 2**15))
            y_values = hist / np.max(hist) * 255  # Scale to 0-255 for intensity

            # Shift pixel buffer downwards
            pixel_buffer[1:, :] = pixel_buffer[:-1, :]

            # Add new values to the top of the buffer
            for x in range(box_width):
                pixel_buffer[0, x] = (0, int(y_values[x]), 0)  # Green channel based on y_values

            # Draw pixel buffer at the bottom
            frame[histogram_start_y:histogram_start_y + histogram_height, (resolution[0] - box_width) // 2:(resolution[0] + box_width) // 2] = pixel_buffer
            
            # Draw box around the histogram
            cv2.rectangle(frame, 
                          ((resolution[0] - box_width) // 2, histogram_start_y),
                          ((resolution[0] + box_width) // 2, histogram_start_y + histogram_height),
                          (255, 255, 255), 2)
            
            # Write frame to video
            video_writer.write(frame)

        # Release video writer
        video_writer.release()

        # Add audio to the video
        cls.add_audio_to_video(wav_file_path, temp_video_path, output_video_path)

        # Remove temporary video file
        os.remove(temp_video_path)

    @staticmethod
    def add_audio_to_video(audio_path, video_path, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        # Load the video
        video = VideoFileClip(video_path)
        
        # Load the audio
        audio = AudioFileClip(audio_path)
        
        # Set the audio of the video to the loaded audio
        final_video = video.set_audio(audio)
        
        # Write the result to a file
        final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')
        
        # Close the clips
        video.close()
        audio.close()