import tkinter as tk
from tkinter import ttk

import random


def generate_charset(seed=357):
    if seed is not None:
        random.seed(seed)

    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    random.shuffle(alpha)

    extra = list("0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~\"\\")
    return "".join(alpha + extra)


# Then in your encoder:
CHARSET = generate_charset()


def encode(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char in CHARSET:
            index = CHARSET.index(char)
            result += CHARSET[(index + shift) % len(CHARSET)]
        else:
            result += char  # Leave unsupported characters unchanged
    return result

def decode(text: str, shift: int) -> str:
    return encode(text, -shift)


def create_ui():
    def on_encode():
        shift = int(shift_entry.get())
        text = input_text.get("1.0", tk.END).rstrip('\n')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encode(text, shift))

    def on_decode():
        shift = int(shift_entry.get())
        text = input_text.get("1.0", tk.END).rstrip('\n')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decode(text, shift))

    # GUI setup
    root = tk.Tk()
    root.title("Simple Text Encoder/Decoder")

    ttk.Label(root, text="Input Text:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    input_text = tk.Text(root, height=5, width=60)
    input_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    ttk.Label(root, text="Shift:").grid(row=2, column=0, padx=5, sticky="e")
    shift_entry = ttk.Entry(root, width=5)
    shift_entry.insert(0, "8")
    shift_entry.grid(row=2, column=1, padx=5, sticky="w")

    ttk.Button(root, text="Encode", command=on_encode).grid(row=2, column=2, sticky="w", padx=5)
    ttk.Button(root, text="Decode", command=on_decode).grid(row=2, column=2, sticky="e", padx=5)

    ttk.Label(root, text="Output Text:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    output_text = tk.Text(root, height=5, width=60)
    output_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
