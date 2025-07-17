import tkinter as tk
from tkinter import ttk
import random


def generate_charset(seed: int = 0):
    rng = random.Random(seed)  # Local RNG instance
    charset = list(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
        "!@#$%^&*()-_=+[]{}|;:',.<>?/`~\"\\"
    )
    rng.shuffle(charset)
    return ''.join(charset)


def encode(text: str, charset: str, shift: int) -> str:
    result = ""
    for char in text:
        if char in charset:
            index = charset.index(char)
            result += charset[(index + shift) % len(charset)]
        else:
            result += char
    return result


def decode(text: str, charset: str, shift: int) -> str:
    return encode(text, charset, -shift)


class EncoderDecoderUI():
    def __init__(self, seed: int, shift: int):
        # --- GUI setup ---
        self.root = tk.Tk()
        self.root.title("Text Encoder/Decoder with Seed")
        self.root.geometry("600x300")
        self.root.resizable(True, True)

        # --- Configure grid to be resizable ---
        for col in range(4):
            self.root.columnconfigure(col, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(5, weight=1)

        # --- Widgets ---
        ttk.Label(self.root, text="Input Text:").grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.input_text = tk.Text(self.root, height=5)
        self.input_text.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        ttk.Label(self.root, text="Shift:").grid(row=2, column=0, padx=5, sticky="e")
        self.shift_entry = ttk.Entry(self.root, width=5)
        self.shift_entry.insert(0, str(shift))
        self.shift_entry.grid(row=2, column=1, padx=5, sticky="w")

        ttk.Label(self.root, text="Seed:").grid(row=2, column=2, padx=5, sticky="e")
        self.seed_entry = ttk.Entry(self.root, width=10)
        self.seed_entry.insert(0, str(seed))
        self.seed_entry.grid(row=2, column=3, padx=5, sticky="w")

        ttk.Button(self.root, text="Encode", command=self.on_encode).grid(row=3, column=1, sticky="w", padx=5, pady=5)
        ttk.Button(self.root, text="Decode", command=self.on_decode).grid(row=3, column=2, sticky="e", padx=5, pady=5)

        ttk.Label(self.root, text="Output Text:").grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.output_text = tk.Text(self.root, height=5)
        self.output_text.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        self.root.mainloop()


    def get_seed_and_shift(self):
        try:
            shift = int(self.shift_entry.get())
            seed = int(self.seed_entry.get())
        except ValueError:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Error: Shift and Seed must be integers.")
        return seed, shift


    def on_encode(self):
        shift, seed = self.get_seed_and_shift()
        charset = generate_charset(seed)
        text = self.input_text.get("1.0", tk.END).rstrip('\n')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, encode(text, charset, shift))


    def on_decode(self):
        shift, seed = self.get_seed_and_shift()
        charset = generate_charset(seed)
        text = self.input_text.get("1.0", tk.END).rstrip('\n')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, decode(text, charset, shift))


if __name__ == "__main__":
    EncoderDecoderUI(357, 8)
