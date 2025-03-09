import os
import shutil
from PIL import Image


class ImageProselyte:
    @classmethod
    def ImageToPNG(cls, input_path, output_path):
        cls._process_image(input_path, output_path, 'PNG')

    @classmethod
    def ImageToJPEG(cls, input_path, output_path):
        cls._process_image(input_path, output_path, 'JPEG')

    @classmethod
    def ImageToBMP(cls, input_path, output_path):
        cls._process_image(input_path, output_path, 'BMP')

    @classmethod
    def ImageToGIF(cls, input_path, output_path):
        cls._process_image(input_path, output_path, 'GIF')

    @classmethod
    def ImageToTIFF(cls, input_path, output_path):
        cls._process_image(input_path, output_path, 'TIFF')

    @classmethod
    def ImageToWebP(cls, input_path, output_path):
        cls._process_image(input_path, output_path, 'WebP')

    @classmethod
    def ImageToICO(cls, input_path, output_path):
        cls._process_image(input_path, output_path, 'ICO')

    @classmethod
    def ImageToPPM(cls, input_path, output_path):
        cls._process_image(input_path, output_path, 'PPM')

    @classmethod
    def ImageToPCX(cls, input_path, output_path):
        cls._process_image(input_path, output_path, 'PCX')

    @classmethod
    def ImageToEPS(cls, input_path, output_path):
        cls._process_image(input_path, output_path, 'EPS')

    @classmethod
    def _process_image(cls, input_path, output_path, format):
        if os.path.isdir(input_path):
            cls._process_directory(input_path, output_path, format)
        else:
            cls._process_file(input_path, output_path, format)

    @classmethod
    def _process_directory(cls, input_dir, output_dir, format):
        for root, _, files in os.walk(input_dir):
            for file in files:
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_dir)
                current_output_dir = os.path.join(output_dir, relative_path)
                
                if os.path.basename(current_output_dir) == os.path.basename(output_dir):
                    current_output_dir = output_dir
                
                os.makedirs(current_output_dir, exist_ok=True)
                cls._process_file(input_file, current_output_dir, format)

    @classmethod
    def _process_file(cls, input_file, output_dir, format):
        try:
            if not os.path.exists(input_file):
                return

            if not cls._is_image_file(input_file):
                return

            output_filename = f"{os.path.splitext(os.path.basename(input_file))[0]}.{format.lower()}"
            output_path = os.path.join(output_dir, output_filename)

            with Image.open(input_file) as img:
                if img.mode in ('RGBA', 'LA') and format in ['JPEG', 'BMP']:
                    img = img.convert('RGB')
                
                if format == 'JPEG':
                    img.save(output_path, format=format, quality=95, optimize=True)
                elif format == 'PNG':
                    img.save(output_path, format=format, optimize=True)
                elif format == 'WebP':
                    img.save(output_path, format=format, quality=95, method=6)
                elif format == 'TIFF':
                    img.save(output_path, format=format, compression='tiff_lzw')
                else:
                    img.save(output_path, format=format)

        except Exception as e:
            print(f"Error processing {input_file}: {str(e)}")

    @staticmethod
    def _is_image_file(file_path):
        image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp', '.ico', '.ppm', '.pcx', '.eps']
        return os.path.splitext(file_path)[1].lower() in image_extensions