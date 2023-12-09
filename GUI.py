import tkinter as tk

gui = tk.Tk()

gui.title("Placeholder for GUI Title")

gui.geometry("500x500")


load_audio_file_button = tk.Button(gui, text='Load Audio File')

load_audio_file_button.pack(side='bottom',anchor='w',padx=5)

combine_plots_to_single=tk.Button(gui,text="Combine Plots")

combine_plots_to_single.pack(side='bottom',anchor='center',padx=5)

visual_data_btn=tk.Button(gui,text="Visualize Data")

visual_data_btn.pack(side='bottom',anchor='e',padx=5)





gui.mainloop()
