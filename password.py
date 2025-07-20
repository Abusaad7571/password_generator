import tkinter as tk
from tkinter import messagebox
from random import choice
from string import ascii_letters, digits, punctuation

# Password Generator Logic
def create_password(length):
    if length < 4:
        return None
    characters = ascii_letters + digits + punctuation
    return ''.join(choice(characters) for _ in range(length))

# Generate Button Handler
def handle_generate():
    try:
        length_val = int(length_input.get())
        password = create_password(length_val)
        if password:
            result_display.config(text=f"🔐 Generated Password:\n{password}")
        else:
            messagebox.showwarning("Too Short", "Please enter at least 4 characters.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Only whole numbers are allowed.")

# Clear Button Handler
def clear_fields():
    length_input.delete(0, tk.END)
    result_display.config(text="")

# GUI Window Setup
window = tk.Tk()
window.title("CodSoft Internship - Task 1: Password Generator")
window.geometry("440x300")
window.configure(bg="#f0f4f7")

# Heading Label
heading = tk.Label(window, text="🔐 CodSoft Password Generator", 
                   font=("Segoe UI", 16, "bold"), bg="#f0f4f7", fg="#2c3e50")
heading.pack(pady=12)

# Prompt Label
prompt = tk.Label(window, text="Enter desired password length:", 
                  font=("Segoe UI", 12), bg="#f0f4f7", fg="#34495e")
prompt.pack()

# Length Input Field
length_input = tk.Entry(window, font=("Segoe UI", 13), justify="center", width=12, bg="#ffffff", fg="#2c3e50", relief="solid")
length_input.pack(pady=6)

# Button Frame
btn_frame = tk.Frame(window, bg="#f0f4f7")
btn_frame.pack(pady=5)

# Generate Button
generate_btn = tk.Button(btn_frame, text="Generate", command=handle_generate, 
                         font=("Segoe UI", 11, "bold"), bg="#2980b9", fg="white", width=12, relief="flat")
generate_btn.grid(row=0, column=0, padx=10)

# Clear Button
clear_btn = tk.Button(btn_frame, text="Clear", command=clear_fields, 
                      font=("Segoe UI", 11, "bold"), bg="#e74c3c", fg="white", width=10, relief="flat")
clear_btn.grid(row=0, column=1)

# Result Display Label
result_display = tk.Label(window, text="", font=("Segoe UI", 11), bg="#f0f4f7", fg="#2c3e50", wraplength=400, justify="center")
result_display.pack(pady=20)

# Run GUI
window.mainloop()
