import numpy as np
from PIL import Image
import os

#Currently Untested

class ImagePixelValues:
    @classmethod
    def png_to_list(cls, png_file_path):
        if not os.path.exists(png_file_path):
            raise FileNotFoundError(f"The file {png_file_path} does not exist.")
        try:
            with Image.open(png_file_path) as img:
                # Convert image to RGB mode if it's not already
                img = img.convert('RGB')
                # Convert image to numpy array
                img_array = np.array(img)
                # Convert numpy array to nested list
                return img_array.tolist()
        except Exception as e:
            raise IOError(f"Error reading PNG file {png_file_path}: {str(e)}")

    @classmethod
    def list_to_png(cls, rgb_list, output_file):
        try:
            # Convert nested list to numpy array
            img_array = np.array(rgb_list, dtype=np.uint8)
            
            # Create image from numpy array
            img = Image.fromarray(img_array, 'RGB')
            
            # Save image as PNG
            img.save(output_file, 'PNG')
            
            print(f"Successfully wrote PNG file to {output_file}")
        except Exception as e:
            raise IOError(f"Error writing PNG file {output_file}: {str(e)}")