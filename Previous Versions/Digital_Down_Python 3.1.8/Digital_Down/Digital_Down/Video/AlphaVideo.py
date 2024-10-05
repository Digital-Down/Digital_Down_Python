import cv2
import numpy as np
import os

class AlphaVideo:
    @classmethod
    def black(cls, tolerance, video_path, output_dir):
        cls._process_video(tolerance, video_path, output_dir, (0, 0, 0))
    
    @classmethod
    def white(cls, tolerance, video_path, output_dir):
        cls._process_video(tolerance, video_path, output_dir, (255, 255, 255))

    @classmethod
    def green(cls, tolerance, video_path, output_dir):
        cls._process_video(tolerance, video_path, output_dir, (0, 255, 0))
    
    @classmethod
    def red(cls, tolerance, video_path, output_dir):
        cls._process_video(tolerance, video_path, output_dir, (0, 0, 255))
    
    @classmethod
    def blue(cls, tolerance, video_path, output_dir):
        cls._process_video(tolerance, video_path, output_dir, (255, 0, 0))
    
    @classmethod
    def _process_video(cls, tolerance, video_path, output_dir, transparent_color):
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print("Error: Could not open the video file.")
            return

        fps = cap.get(cv2.CAP_PROP_FPS)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_alpha = cls._make_transparent(frame, transparent_color, tolerance)
            output_path = os.path.join(output_dir, f'frame_{frame_count:04d}.png')
            cv2.imwrite(output_path, frame_alpha)

            frame_count += 1

        cap.release()
        cv2.destroyAllWindows()

        print(f"Processed {frame_count} frames at {fps} FPS.")

    @staticmethod
    def _make_transparent(frame, color, tolerance):
        h, w = frame.shape[:3]
        transparent_frame = np.zeros((h, w, 4), dtype=np.uint8)

        if color == (255, 255, 255):
            mask = cv2.inRange(frame, np.array([255-tolerance]*3), np.array([255, 255, 255]))
        elif color == (0, 0, 0):
            mask = cv2.inRange(frame, np.array([0, 0, 0]), np.array([tolerance]*3))
        elif color == (0, 255, 0):
            mask = cv2.inRange(frame, np.array([0, 255-tolerance, 0]), np.array([tolerance, 255, tolerance]))
        elif color == (0, 0, 255):
            mask = cv2.inRange(frame, np.array([0, 0, 255-tolerance]), np.array([tolerance, tolerance, 255]))
        elif color == (255, 0, 0):
            mask = cv2.inRange(frame, np.array([255-tolerance, 0, 0]), np.array([255, tolerance, tolerance]))

        transparent_frame[:, :, :3] = frame
        transparent_frame[:, :, 3] = 255 - mask

        return transparent_frame

