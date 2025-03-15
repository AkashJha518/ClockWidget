import tkinter as tk
from time import strftime

def update_time():
    """Update the time and date every second."""
    current_time = strftime("%H:%M:%S")  # Time (HH:MM:SS)
    current_date = strftime("%Y-%m-%d")  # Date (YYYY-MM-DD)
    
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    root.after(1000, update_time)  # Refresh every second

# Create main window
root = tk.Tk()
root.title("Transparent Clock")

# Remove window decorations (borderless)
root.overrideredirect(True)

# Get screen width & height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size and position (rightmost bottom corner)
window_width = 250  
window_height = 100  
x_position = (screen_width - window_width)//2
y_position = (screen_height - window_height-250)//2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
Background = "#93DCE3"
textcolor = "white"
# Set window transparency (fixes blurry text issue)
root.config(bg=Background)  # Background color to blend better
root.attributes("-transparentcolor", Background)  # 0.0 = fully transparent, 1.0 = fully visible
root.lower()
root.attributes("-topmost", False)
# Time Label (Black Font, Transparent Background)
time_label = tk.Label(root, text="", font=("Microsoft Sans Serif", 40, "bold"), fg=textcolor, bg=Background, bd=0)
time_label.pack()

# Date Label (Smaller Font, Black Text, Transparent Background)
date_label = tk.Label(root, text="", font=("Helvetica", 20), fg=textcolor, bg=Background, bd=0)
date_label.pack()

# Start clock update
update_time()

# Run the application
root.mainloop()
