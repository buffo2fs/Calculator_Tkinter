# Tkinter is library to create graphic interfaces in Python

import tkinter as tk

# Evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        output.config(text=f"Result: {result}", fg="#2ecc71") # Green text for success
    
    except Exception:
        output.config(text="Error", fg="#e74c3c") # Red text for error

# Create Window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x250") # set window size
window.configure(bg="#2c3e50") # dark background

# Title Label
title = tk.Label(window, text="Simple Calculator", font=("Arial", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
title.pack(pady=10)

# Input Field
entry = tk.Entry(window, width=25, font=("Arial", 16), borderwidth=5, relief="ridge", justify="center")
entry.pack(pady=10)

# Calculate Button
button = tk.Button(
    window, text="Calculate", command=calculate, 
    font=("Arial", 12, "bold"), bg="#3498db", fg="white",
    activebackground="#2980b9", activeforeground="white",
    relief="flat", padx=20, pady=5
    )
button.pack(pady=10)

# Output label
output = tk.Label(window, text="Result: ", font=("Arial", 14, "bold"), bg="#2c3e50", fg="#ecf0f1")
output.pack(pady=10)

# Main loop

window.mainloop()
