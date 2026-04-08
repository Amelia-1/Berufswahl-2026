
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 
import openpyxl
import pandas as pd
import themes 
from appui import *
from classes import *

tabelle = None

#DEV OPTIONS
NO_UI = True

def get_filepath():
    filepath = filedialog.askopenfilename(
        title="Eine Datei Auswählen",
        filetypes=(("Excel Datei", "*.xlsx"),)
    )
    return filepath
    
    
def read_data():
    filepath = get_filepath()
    global tabelle
    tabelle = pd.read_excel(filepath, header=None)

    data = tabelle.iloc[0,0]
    
    
print("aaa")






