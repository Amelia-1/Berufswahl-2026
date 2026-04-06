from tkinter import ttk

def apply_dark_theme(root):

    style = ttk.Style(root)
    style.theme_use('clam')

    DARK_BG = "#1e1e1e"
    LIGHT_FG = "#ffffff"
    ACCENT_COLOR = "#3d5afe"    
    HOVER_COLOR = "#536dfe"
    PRESSED_COLOR = "#283593"


    root.configure(bg=DARK_BG)

    style.configure(
        "TFrame",
        background=DARK_BG
    )

    style.configure(
        "BigTitle.TLabel", 
        font=("Helvetica", 72, "bold"),
        background=DARK_BG, 
        foreground=LIGHT_FG
    )

    style.configure(
        "TButton",
        font=("Segoe UI", 13, "bold"),
        foreground=LIGHT_FG,
        background=ACCENT_COLOR,
        padding=(35, 12),      # Modern wide-button look
        borderwidth=0,
        
    )

    style.map(
        "TButton",
        background=[
            ('pressed', PRESSED_COLOR), 
            ('active', HOVER_COLOR)
        ],
        # Adds a slight "push down" effect when clicked
        shiftrelief=[('pressed', 1)]
    )