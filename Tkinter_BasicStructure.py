# Tkinter is library to create graphic interfaces in Python

import tkinter as tk

# Evaluate the expression

def calculate():
    try:
        result = eval(entry.get())
        output.config(text=f"Result: {result}")
    
    except Exception as e:
        output.config(text="Error")

# Create Window

window = tk.Tk()
window.title("Simple Calculator")

# Input Field

entry = tk.Entry(window, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Calculate Button

button = tk.Button(window, text="Calculate", command=calculate, font=("Arial", 12))
button.pack(pady=5)

# Output label

output = tk.Label(window, text="Result: ", font=("Arial", 22))
output.pack(pady=10)

# Main loop

window.mainloop()


