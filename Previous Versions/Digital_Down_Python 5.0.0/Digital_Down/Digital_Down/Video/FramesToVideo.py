import cv2
import os

class FramesToVideo:
    @classmethod
    def create_video(cls, frames_folder, output_path, fps):
        # Get list of image files
        images = [img for img in os.listdir(frames_folder) if img.endswith(".png")]
        images.sort()

        if not images:
            print("No images found in the specified folder.")
            return

        # Read the first image to get the dimensions
        first_frame_path = os.path.join(frames_folder, images[0])
        frame = cv2.imread(first_frame_path, cv2.IMREAD_UNCHANGED)
        height, width, layers = frame.shape

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        for image in images:
            img_path = os.path.join(frames_folder, image)
            frame = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
            if frame.shape[2] == 4:  # Check if the image has an alpha channel
                # Separate the alpha channel and merge it with a black background
                bgr = frame[:, :, :3]
                alpha = frame[:, :, 3]
                frame = cv2.merge((bgr, alpha))
            video.write(frame)

        video.release()
        print(f"Video saved as {output_path}")

