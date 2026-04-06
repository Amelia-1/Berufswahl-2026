
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 
import openpyxl
import pandas as pd
import themes 



def get_filepath():
    filepath = filedialog.askopenfilename(
        title="Eine Datei Auswählen",
        filetypes=(("Excel Datei", "*.xlsx"),)
    )
    return filepath
    
    
def read_data():
    filepath = get_filepath()
    tabelle = pd.read_excel(filepath, header=None)

    data = tabelle.iloc[0,0]
    
    
def exit(event=None):
    root.destroy()


root = tk.Tk()
root.title("BU 2026")
root.attributes("-fullscreen",True)
root.bind("<Escape>", exit)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

style = themes.apply_dark_theme(root) 

# --- MAIN FRAME ---
main_frame = ttk.Frame(root)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure((0, 1), weight=1)
main_frame.grid(row=0, column=0, sticky="nsew")


title = ttk.Label(main_frame, text="Berufswahl 2026", style="BigTitle.TLabel")
title.grid(row=0, column=0, sticky="s")

select_button = ttk.Button(main_frame, text="Select File", command=read_data)
select_button.grid(row=1, column=0, sticky="n", pady=20)

root.mainloop()



