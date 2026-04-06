
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 
import openpyxl
import pandas as pd
import themes 
from PIL import ImageTk, Image



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
    
    
def exit_app(event=None):
    root.destroy()


root = tk.Tk()
root.title("BU 2026")
#root.attributes("-fullscreen",True)
root.state("zoomed")
root.bind("<Escape>", exit_app)





'''
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
'''

style = themes.apply_dark_theme(root) 


# --- MAIN FRAME ---
main_frame = ttk.Frame(root)

main_frame.pack(fill="both", expand=True)

'''
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure((0, 1, 2), weight=1)
main_frame.grid(row=0, column=0, sticky="nsew")
'''

logo_container = ttk.Frame(main_frame)
logo_container.pack(side="top", anchor="nw", padx=30, pady=30)
original_logo = Image.open("logo.png")
original_logo.thumbnail((400, 400)) 
tk_logo = ImageTk.PhotoImage(original_logo)
logo_label = tk.Label(main_frame, image=tk_logo, bg="#181617", borderwidth=0, anchor="center")
logo_label.image = tk_logo 
logo_label.place(relx=0.5,rely=0.2, anchor="center")







# Create an invisible container for the content
content_frame = ttk.Frame(main_frame)
content_frame.pack(expand=True) # This centers the entire block



# Title inside the content frame
title = ttk.Label(
    content_frame, 
    text="[BERUFSWAHL 2026]", 
    style="BigTitle.TLabel",
    anchor="center"
)
title.pack(pady=(0, 10)) 

# Add a subtitle for better "editorial" look
subtitle = ttk.Label(
    content_frame,
    text="WÄHLEN SIE IHRE EXCEL-TABELLE AUS, UM ZU BEGINNEN",
    style = "Subtitle.TLabel"
)
subtitle.pack(pady=(30, 20)) # Larger gap before button

# Button inside the content frame
select_button = ttk.Button(
    content_frame, 
    text="TABELLE AUSWÄHLEN", 
    command=read_data
)
select_button.pack()

root.mainloop()



