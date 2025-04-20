import tkinter as tk

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

# Generate button (placeholder for now)
def on_generate():
    print("Generate button clicked!")  # Placeholder action

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Generated Password will appear here.")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()