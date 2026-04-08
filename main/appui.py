import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 
import openpyxl
import pandas as pd
import themes 
from PIL import ImageTk, Image
from start import *


def exit_app(event=None):
    root.destroy()




root = tk.Tk()
root.title("BU 2026")
#root.attributes("-fullscreen",True)
root.state("zoomed")
root.bind("<Escape>", exit_app)



style = themes.apply_dark_theme(root) 


# --- MAIN FRAME ---
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True)



# --- LOGO ---
logo_container = ttk.Frame(main_frame)
logo_container.pack(side="top", anchor="nw", padx=30, pady=30)
original_logo = Image.open("logo.png")
original_logo.thumbnail((400, 400)) 
tk_logo = ImageTk.PhotoImage(original_logo)
logo_label = tk.Label(main_frame, image=tk_logo, bg="#181617", borderwidth=0, anchor="center")
logo_label.image = tk_logo 
logo_label.place(relx=0.5,rely=0.2, anchor="center")



content_frame = ttk.Frame(main_frame)
content_frame.pack(expand=True) 




title = ttk.Label(
    content_frame, 
    text="[BERUFSWAHL 2026]", 
    style="BigTitle.TLabel",
    anchor="center"
)
title.pack(pady=(0, 10)) 

subtitle = ttk.Label(
    content_frame,
    text="WÄHLEN SIE IHRE EXCEL-TABELLE AUS, UM ZU BEGINNEN",
    style = "Subtitle.TLabel"
)
subtitle.pack(pady=(30, 20)) 

select_button = ttk.Button(
    content_frame, 
    text="TABELLE AUSWÄHLEN", 
    command=read_data
)
select_button.pack()

root.mainloop()