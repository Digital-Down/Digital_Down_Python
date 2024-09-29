import cv2
import numpy as np
import os

#Currently Untested

class VideoPixelValues:
    @classmethod
    def video_to_list(cls, video_file_path):
        if not os.path.exists(video_file_path):
            raise FileNotFoundError(f"The file {video_file_path} does not exist.")
        try:
            cap = cv2.VideoCapture(video_file_path)
            frames = []
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                # Convert BGR to RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frames.append(frame_rgb.tolist())
            
            cap.release()
            return frames
        except Exception as e:
            raise IOError(f"Error reading video file {video_file_path}: {str(e)}")

    @classmethod
    def list_to_video(cls, frames_list, output_file, fps=30.0, codec='mp4v'):
        try:
            if not frames_list:
                raise ValueError("The input frames list is empty.")
            
            # Convert the first frame to numpy array to get dimensions
            first_frame = np.array(frames_list[0], dtype=np.uint8)
            height, width, _ = first_frame.shape
            
            fourcc = cv2.VideoWriter_fourcc(*codec)
            out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
            
            for frame in frames_list:
                # Convert list to numpy array
                frame_array = np.array(frame, dtype=np.uint8)
                # Convert RGB to BGR
                frame_bgr = cv2.cvtColor(frame_array, cv2.COLOR_RGB2BGR)
                out.write(frame_bgr)
            
            out.release()
            print(f"Successfully wrote video file to {output_file}")
        except Exception as e:
            raise IOError(f"Error writing video file {output_file}: {str(e)}")

    @classmethod
    def mov_to_list(cls, mov_file_path):
        return cls.video_to_list(mov_file_path)

    @classmethod
    def avi_to_list(cls, avi_file_path):
        return cls.video_to_list(avi_file_path)

    @classmethod
    def list_to_mov(cls, frames_list, output_file, fps=30.0):
        return cls.list_to_video(frames_list, output_file, fps, codec='mp4v')

    @classmethod
    def list_to_avi(cls, frames_list, output_file, fps=30.0):
        return cls.list_to_video(frames_list, output_file, fps, codec='XVID')