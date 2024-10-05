import cv2
import numpy as np
import os

class AlphaImage:
    @classmethod
    def black(cls, tolerance, image_path, output_path):
        cls._process_image(tolerance, image_path, output_path, (0, 0, 0))
    
    @classmethod
    def white(cls, tolerance, image_path, output_path):
        cls._process_image(tolerance, image_path, output_path, (255, 255, 255))

    @classmethod
    def green(cls, tolerance, image_path, output_path):
        cls._process_image(tolerance, image_path, output_path, (0, 255, 0))
    
    @classmethod
    def red(cls, tolerance, image_path, output_path):
        cls._process_image(tolerance, image_path, output_path, (0, 0, 255))
    
    @classmethod
    def blue(cls, tolerance, image_path, output_path):
        cls._process_image(tolerance, image_path, output_path, (255, 0, 0))
    
    @classmethod
    def _process_image(cls, tolerance, image_path, output_path, transparent_color):
        image = cv2.imread(image_path)

        if image is None:
            print("Error: Could not open the image file.")
            return

        image_alpha = cls._make_transparent(image, transparent_color, tolerance)
        cv2.imwrite(output_path, image_alpha)

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
