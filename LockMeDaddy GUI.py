import tkinter as tk
from tkinter import messagebox
import random

# Function to generate the password
def on_generate():
    try:
        # Get user inputs
        num_letters = int(entry_letters.get())
        num_symbols = int(entry_symbols.get())
        num_numbers = int(entry_numbers.get())

        if num_letters < 0 or num_symbols < 0 or num_numbers < 0:
            messagebox.showerror("Error", "Please enter non-negative numbers.")
            return
        elif num_letters > 15 and num_symbols > 15 and num_numbers > 15:
            messagebox.showerror("Error", "The maximun number of characters for each category is 15.")
            return

        
        # Define character pools
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        symbols = '!@#$%^&*()-_=+{}[]:;\'"<>,.?/|'
        numbers = '0123456789'

        # Generate random characters
        password_letters = random.choices(letters, k=num_letters)
        password_symbols = random.choices(symbols, k=num_symbols)
        password_numbers = random.choices(numbers, k=num_numbers)

        # Combine and shuffle the password
        password = password_letters + password_symbols + password_numbers
        random.shuffle(password)

        # Display the result
        result_label.config(text="Generated Password: " + ''.join(password))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers only.")

# Create the GUI window
root = tk.Tk()
root.title("Password Generator")

# Input fields
tk.Label(root, text="Number of Letters:").grid(row=0, column=0, padx=10, pady=5)
entry_letters = tk.Entry(root)
entry_letters.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Number of Symbols:").grid(row=1, column=0, padx=10, pady=5)
entry_symbols = tk.Entry(root)
entry_symbols.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Number of Numbers:").grid(row=2, column=0, padx=10, pady=5)
entry_numbers = tk.Entry(root)
entry_numbers.grid(row=2, column=1, padx=10, pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()