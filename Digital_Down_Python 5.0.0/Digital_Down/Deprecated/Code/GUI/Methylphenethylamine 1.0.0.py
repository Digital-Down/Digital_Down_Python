import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from .Methylphenethylamine import *
from .AudioSampleValues import *
import base64
import sys




# Blank icon (1x1 transparent GIF)
BLANK_ICON = base64.b64decode(b'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7')


class MethylphenethylamineGUI:
    def __init__(self, master):
        master.configure(background='#2b2b2b')
        master.option_add('*Font', 'Helvetica 10')

        self.master = master
        master.title("Digital Down's Methylphenethylamine 1.0.0")
        master.geometry("500x250")
        master.resizable(False, False)  # Fixed window size
        # Set blank icon
        self.icon = tk.PhotoImage(data=BLANK_ICON)
        master.iconphoto(True, self.icon)

        # Load the background image
        #self.background_image = tk.PhotoImage(file='test.png')
        if getattr(sys, 'frozen', False):
            self.background_image = tk.PhotoImage(file=os.path.join(sys._MEIPASS, 'Background.png'))
        else:
            self.background_image = tk.PhotoImage(file='Background.png')

        # Create a label with the background image
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(x=0, y=0, width=500, height=250)

        # Keep a reference to the image to prevent it from being garbage collected
        self.background_label.image = self.background_image

        self.input_file = tk.StringVar()
        self.output_file = tk.StringVar()
        self.stretch_mode = tk.IntVar(value=0)

        # Input file selection
        tk.Label(master, text="Input WAV:", foreground='#ffffff', background='#000000', highlightthickness=0).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(master, textvariable=self.input_file, width=40, foreground='#ffffff', background='#000000', highlightthickness=0).grid(row=0, column=1, columnspan=2, padx=10, pady=5)
        tk.Button(master, text="Browse", command=self.browse_input, foreground='#ffffff', background='#000000', highlightthickness=0).grid(row=0, column=3, padx=10, pady=5)

        # Output file selection
        tk.Label(master, text="Output WAV:", foreground='#ffffff', background='#000000', highlightthickness=0).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(master, textvariable=self.output_file, width=40, foreground='#ffffff', background='#000000', highlightthickness=0).grid(row=1, column=1, columnspan=2, padx=10, pady=5)
        tk.Button(master, text="Browse", command=self.browse_output, foreground='#ffffff', background='#000000', highlightthickness=0).grid(row=1, column=3, padx=10, pady=5)

        # Stretch mode selection
        stretch_frame = tk.Frame(master, background='#000000', highlightthickness=0)
        stretch_frame.grid(row=2, column=0, columnspan=4, pady=10)
        modes = [("-1", -1), ("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5)]
        for i, (text, value) in enumerate(modes):
            tk.Radiobutton(stretch_frame, text=text, variable=self.stretch_mode, value=value, foreground='#ffffff', background='#000000', highlightthickness=0, selectcolor='#2b2b2b').grid(row=0, column=i, padx=10)
        # Run button
        self.run_button = tk.Button(master, text="Speed", command=self.run_stretch, background='#000000', foreground='#ffffff')
        self.run_button.grid(row=3, column=1, columnspan=2, pady=10, padx=10)
        self.run_button.config(state=tk.DISABLED)  # <--- Add this line

        # Progress bar
        self.progress = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate", style='Horizontal.TProgressbar')
        self.progress.grid(row=4, column=0, columnspan=4, pady=10, padx=10)

        # Supported file formats label
        supported_formats_label = tk.Label(master, text="Currently only supports 16-bit, 44100 Samples WAV files", background='#000000', foreground='#ffffff')
        supported_formats_label.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

        # Bind events to update run button state
        self.input_file.trace_add("write", self.update_run_button_state)
        self.output_file.trace_add("write", self.update_run_button_state)
        self.stretch_mode.trace_add("write", self.update_run_button_state)

    def browse_input(self):
        filename = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if filename:
            self.input_file.set(filename)

    def browse_output(self):
        filename = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
        if filename:
            self.output_file.set(filename)

    def update_run_button_state(self, *args):
        if self.input_file.get() and self.output_file.get() and self.stretch_mode.get() != 0:
            self.run_button.config(state=tk.NORMAL)
        else:
            self.run_button.config(state=tk.DISABLED)

    def run_stretch(self):
        input_wav = self.input_file.get()
        output_wav = self.output_file.get()
        mode = self.stretch_mode.get()

        try:
            samples = AudioSampleValues.wav_to_list(input_wav)
            self.progress['value'] = 20
            self.master.update_idletasks()

            if mode == -1:
                modified_samples = Methylphenethylamine.slow([samples], 1)
            else:
                modified_samples = Methylphenethylamine.fast([samples], mode)
            self.progress['value'] = 60
            self.master.update_idletasks()
            AudioSampleValues.list_to_wav(modified_samples, output_wav)
            self.progress['value'] = 100
            self.master.update_idletasks()

            messagebox.showinfo("Success", "Audio processing completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.progress['value'] = 0

if __name__ == "__main__":
    root = tk.Tk()
    gui = MethylphenethylamineGUI(root)
    root.mainloop()

#Exe string in command prompt: pyinstaller --onefile --windowed --hidden-import=Audio.Methylphenethlamine --hidden-import=Audio.AudioSampleValues --add-data "Background.png;." "Methylphenethylamine 1.0.0.py"