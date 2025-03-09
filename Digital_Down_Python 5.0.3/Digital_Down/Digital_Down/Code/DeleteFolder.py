import os
import shutil

class DeleteFolder:
    def Delete(self, folder_path, folder_to_delete):
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for dir in dirs:
                if dir == folder_to_delete:
                    path_to_remove = os.path.join(root, dir)
                    try:
                        shutil.rmtree(path_to_remove)
                        print(f"Deleted folder and its contents: {path_to_remove}")
                    except Exception as e:
                        print(f"Error deleting {path_to_remove}: {e}")