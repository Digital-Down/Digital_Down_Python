import cv2
import numpy as np

class AlphaOver:
    @classmethod
    def black(cls, tolerance, video1_path, video2_path, output_path):
        cls._alpha_over(video1_path, video2_path, output_path, transparent_color=(0, 0, 0), tolerance=tolerance)
    
    @classmethod
    def white(cls, tolerance, video1_path, video2_path, output_path):
        cls._alpha_over(video1_path, video2_path, output_path, transparent_color=(255, 255, 255), tolerance=tolerance)

    @classmethod
    def green(cls, tolerance, video1_path, video2_path, output_path):
        cls._alpha_over(video1_path, video2_path, output_path, transparent_color=(0, 255, 0), tolerance=tolerance)
    
    @classmethod
    def red(cls, tolerance, video1_path, video2_path, output_path):
        cls._alpha_over(video1_path, video2_path, output_path, transparent_color=(0, 0, 255), tolerance=tolerance)
    
    @classmethod
    def blue(cls, tolerance, video1_path, video2_path, output_path):
        cls._alpha_over(video1_path, video2_path, output_path, transparent_color=(255, 0, 0), tolerance=tolerance)
    
    @classmethod
    def _alpha_over(cls, video1_path, video2_path, output_path, transparent_color, tolerance):
        cap1 = cv2.VideoCapture(video1_path)
        cap2 = cv2.VideoCapture(video2_path)

        if not cap1.isOpened() or not cap2.isOpened():
            print("Error: Could not open one of the video files.")
            return

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        fps = int(cap1.get(cv2.CAP_PROP_FPS))
        width = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        while True:
            ret1, frame1 = cap1.read()
            ret2, frame2 = cap2.read()

            if not ret1 or not ret2:
                break

            frame1_alpha = cls._make_transparent(frame1, transparent_color, tolerance)
            combined_frame = cls._overlay_frames(frame1_alpha, frame2)

            out.write(combined_frame)

        cap1.release()
        cap2.release()
        out.release()
        cv2.destroyAllWindows()

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

    @staticmethod
    def _overlay_frames(foreground, background):
        h, w = foreground.shape[:2]
        overlay = np.zeros((h, w, 3), dtype=np.uint8)

        alpha = foreground[:, :, 3] / 255.0
        for c in range(3):
            overlay[:, :, c] = foreground[:, :, c] * alpha + background[:, :, c] * (1 - alpha)

        return overlay