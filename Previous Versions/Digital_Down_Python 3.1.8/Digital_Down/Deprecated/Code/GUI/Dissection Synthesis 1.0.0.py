import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from Audio.DissectionSynthesis import *
import base64

# Blank icon (1x1 transparent GIF)
BLANK_ICON = base64.b64decode(b'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7')

class DissectionSynthesisGUI:
    def __init__(self, master):
        master.configure(background='#2b2b2b')
        master.option_add('*Font', 'Helvetica 10')

        self.master = master
        master.title("Digital Down's DissectionSynthesis 1.0.0")
        master.geometry("500x250")
        master.resizable(False, False)  # Fixed window size
        
        # Set blank icon
        self.icon = tk.PhotoImage(data=BLANK_ICON)
        master.iconphoto(True, self.icon)

        # Load the background image
        self.background_image = tk.PhotoImage(file='Background.png')

        # Create a label with the background image
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Keep a reference to the image to prevent it from being garbage collected
        self.background_label.image = self.background_image

        self.input_folder = tk.StringVar()
        self.output_folder = tk.StringVar()
        self.combine_var = tk.BooleanVar(value=False)

        # Input folder selection
        tk.Label(master, text="Input Folder:", foreground='#ffffff', background='#000000', highlightthickness=0).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(master, textvariable=self.input_folder, width=40, foreground='#ffffff', background='#000000', highlightthickness=0).grid(row=0, column=1, columnspan=2, padx=10, pady=5)
        tk.Button(master, text="Browse", command=self.browse_input, foreground='#ffffff', background='#000000', highlightthickness=0).grid(row=0, column=3, padx=10, pady=5)

        # Output folder selection
        tk.Label(master, text="Output Folder:", foreground='#ffffff', background='#000000', highlightthickness=0).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(master, textvariable=self.output_folder, width=40, foreground='#ffffff', background='#000000', highlightthickness=0).grid(row=1, column=1, columnspan=2, padx=10, pady=5)
        tk.Button(master, text="Browse", command=self.browse_output, foreground='#ffffff', background='#000000', highlightthickness=0).grid(row=1, column=3, padx=10, pady=5)

        # Combine button
        self.combine_button = tk.Button(master, text="Combine: Off", command=self.toggle_combine, background='#000000', foreground='#ffffff')
        self.combine_button.grid(row=2, column=1, columnspan=2, pady=10, padx=10)
        self.combine_button.config(state=tk.DISABLED)

        # Process button
        self.process_button = tk.Button(master, text="Octave+", command=self.run_process, background='#000000', foreground='#ffffff')
        self.process_button.grid(row=3, column=1, columnspan=2, pady=10, padx=10)
        self.process_button.config(state=tk.DISABLED)

        # Progress bar
        self.progress = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate", style='Horizontal.TProgressbar')
        self.progress.grid(row=4, column=0, columnspan=4, pady=10, padx=10)

        # Supported file formats label
        supported_formats_label = tk.Label(master, text="Currently only supports 16-bit, 44100 Samples WAV files", background='#000000', foreground='#ffffff')
        supported_formats_label.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

        # Bind events to update button states
        self.input_folder.trace_add("write", self.update_button_states)
        self.output_folder.trace_add("write", self.update_button_states)

    def browse_input(self):
        folder = filedialog.askdirectory()
        if folder:
            self.input_folder.set(folder)

    def browse_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder.set(folder)

    def update_button_states(self, *args):
        if self.input_folder.get() and self.output_folder.get():
            self.process_button.config(state=tk.NORMAL)
            self.combine_button.config(state=tk.NORMAL)
        else:
            self.process_button.config(state=tk.DISABLED)
            self.combine_button.config(state=tk.DISABLED)

    def toggle_combine(self):
        self.combine_var.set(not self.combine_var.get())
        self.combine_button.config(text=f"Combine: {'On' if self.combine_var.get() else 'Off'}")

    def run_process(self):
        input_folder = self.input_folder.get()
        output_folder = self.output_folder.get()
        combine = self.combine_var.get()

        try:
            wav_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.wav')]
            total_files = len(wav_files)

            for i, wav_file in enumerate(wav_files):
                input_path = os.path.join(input_folder, wav_file)
                DissectionSynthesis.OctavePlus(input_path, output_folder, combine=combine)
                
                # Update progress
                progress_value = int((i + 1) / total_files * 100)
                self.progress['value'] = progress_value
                self.master.update_idletasks()

            messagebox.showinfo("Success", "Audio processing completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.progress['value'] = 0

if __name__ == "__main__":
    root = tk.Tk()
    gui = DissectionSynthesisGUI(root)
    root.mainloop()