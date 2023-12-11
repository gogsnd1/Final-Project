import tkinter as tk
from tkinter import filedialog
from model import AudioModel
from tkinter import messagebox

class GUI(AudioModel):
    def __init__(self):
        self.gui = tk.Tk()

        self.gui.title("RT60 Analysis GUI")

        self.gui.geometry("500x500")
        self.button_frame = tk.Frame()

        self.load_audio_file_button = tk.Button(self.button_frame, text='Load Audio File', command=GUI.open_finder)

        self.label = tk.Label(self.gui, text='Selected file: ')

        self.combine_plots_to_single = tk.Button(self.button_frame, text="Combine Plots")

        self.visual_data_btn = tk.Button(self.button_frame, text="Spectrogram")

        self.rt60_label=tk.Label(self.gui,text='RT60: Not Calculated')

        self.rf_label=tk.Label(self.gui, text='Resonant Frequency: Not Calculated')

        self.df_label=tk.Label(self.gui, text='Dominant Frequency: Not Calculated')

        self.load_audio_file_button.pack(side='left', padx=5)

        self.label.pack(side='top', anchor='center', pady=5, padx=5)

        self.combine_plots_to_single.pack(side='left', padx=5)

        self.visual_data_btn.pack(side='right', padx=5)

        self.button_frame.pack(side='bottom')

        self.rt60_label.pack(side='left')

        self.rf_label.pack(side='left')

        self.df_label.pack(side='left')


    def open_finder(self):
        self.finder = filedialog.askopenfilename(initialdir='/Downloads', title="Selected File:")
        self.label.config(text=f'Selected File: {self.finder}')

    def mainloop(self):
        self.gui.mainloop()

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def update_rt60_label(self, rt60):
        self.rt60_label.config(text=f"RT60 value: ")

    def update_RF_label(self, RF):
        self.rf_label.config(text="Resonant Frequency: ")

    def update_DF_label(self, DF):
        self.df_label.config(text="Dominant Frequency: ")










