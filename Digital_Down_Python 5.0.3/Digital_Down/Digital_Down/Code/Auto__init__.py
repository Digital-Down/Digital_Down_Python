import os
import glob
from pathlib import Path

class Auto__init__:
    """
    Automatically generates an __init__.py file by scanning all subdirectories
    for Python files and creating import statements.
    """
    
    @classmethod
    def generate(cls):
        """
        Class method to generate the Auto__init__.py file.
        Can be called directly with Auto__init__.generate()
        """
        instance = cls()
        instance.scan_directories()
        instance.generate_init_file()
        print(f"Generated {instance.output_file} with imports from {len(instance.imports)} directories")
    
    def __init__(self, root_dir=None):
        """
        Initialize the Auto__init__ class.
        
        Args:
            root_dir (str, optional): Root directory to scan. If None, will use parent directory of 'Code'.
        """
        if root_dir is None:
            # Get the directory containing this script (Code folder)
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Get the parent directory (one folder above Code)
            self.root_dir = os.path.dirname(current_dir)
        else:
            self.root_dir = root_dir
        
        self.output_file = os.path.join(self.root_dir, "Auto__init__.py")
        self.imports = {}
    
    def scan_directories(self):
        """
        Scan all subdirectories for Python files and organize them by directory.
        """
        # Get all subdirectories in the root directory
        subdirs = [d for d in os.listdir(self.root_dir) 
                  if os.path.isdir(os.path.join(self.root_dir, d)) and not d.startswith('.')]
        
        # For each subdirectory, find all Python files
        for subdir in subdirs:
            subdir_path = os.path.join(self.root_dir, subdir)
            python_files = glob.glob(os.path.join(subdir_path, "*.py"))
            
            # Skip empty directories or those with no Python files
            if not python_files:
                continue
                
            # Initialize the directory in the imports dictionary
            self.imports[subdir] = []
            
            # Add each Python file to the imports list for this directory
            for py_file in python_files:
                # Skip __init__.py files
                if os.path.basename(py_file) == "__init__.py":
                    continue
                
                # Get the filename without extension
                module_name = os.path.splitext(os.path.basename(py_file))[0]
                self.imports[subdir].append(module_name)
    
    def generate_init_file(self):
        """
        Generate the Auto__init__.py file with import statements.
        """
        with open(self.output_file, 'w') as f:
            # Sort the directories for consistent output
            for directory in sorted(self.imports.keys()):
                # Write a comment for the directory
                f.write(f"# {directory}\n")
                
                # Sort the modules for consistent output
                for module in sorted(self.imports[directory]):
                    f.write(f"from .{directory}.{module} import *\n")
                
                # Add a blank line after each directory section
                if self.imports[directory]:
                    f.write("\n")

#Auto__init__.generate()