from tkinter import ttk
import ctypes

def dark_title_bar(window):
    
        window.update()
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ctypes.windll.user32.GetParent
        hwnd = get_parent(window.winfo_id())
        rendering_policy = ctypes.c_int(2)
        
        set_window_attribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(rendering_policy), ctypes.sizeof(rendering_policy))

def apply_dark_theme(root):

    style = ttk.Style(root)
    style.theme_use('clam')

    DARK_BG = "#181617"       # Warm obsidian
    LIGHT_FG = "#f2efe9"
    GREY_FG = "#797979"
    ACCENT_COLOR = "#e35d5b"  # Soft crimson/terracotta
    HOVER_COLOR = "#ef4444"
    PRESSED_COLOR = "#b91c1c"

    LABEL_FONT = "Consolas"
    BUTTON_FONT = "Consolas"
    

    root.configure(bg=DARK_BG)

    dark_title_bar(root)

    style.configure(
        "TFrame",
        background=DARK_BG
    )

    style.configure(
          "TLabel",
          background = DARK_BG,
          foreground = LIGHT_FG
    )

    style.configure(
          "Subtitle.TLabel",
          background = DARK_BG,
          foreground = GREY_FG,
          font=(LABEL_FONT, 10),
    )

    style.configure(
        "BigTitle.TLabel", 
        font=(LABEL_FONT, 80, "bold"),
        background=DARK_BG, 
        foreground=LIGHT_FG,
        
    )

    style.configure(
        "TButton",
        font=(BUTTON_FONT, 12, "bold"),
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

    style.configure(
        "Secondary.TButton",
        font=(BUTTON_FONT, 12),
        foreground=GREY_FG, # Grey text
        background=DARK_BG,   # Matches the background perfectly
        padding=(20, 10),
        borderwidth=0
    )
    style.map(
        "Secondary.TButton",
        foreground=[('active', LIGHT_FG)], # Text turns white on hover
        background=[('active', DARK_BG)]
    )

