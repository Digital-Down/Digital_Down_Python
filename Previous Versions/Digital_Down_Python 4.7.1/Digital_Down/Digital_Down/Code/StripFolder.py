import os
import shutil

class StripFolder:
    def strip(self, folder_path, folder_to_delete):
        for root, dirs, files in os.walk(folder_path, topdown=False):
            if os.path.basename(root) == folder_to_delete:
                parent_dir = os.path.dirname(root)
                
                # Move all files to the parent directory
                for file in files:
                    src = os.path.join(root, file)
                    dst = os.path.join(parent_dir, file)
                    shutil.move(src, dst)
                
                # Move all subdirectories to the parent directory
                for dir in dirs:
                    src = os.path.join(root, dir)
                    dst = os.path.join(parent_dir, dir)
                    shutil.move(src, dst)
                
                # Remove the empty directory
                os.rmdir(root)
                print(f"Processed and removed: {root}")