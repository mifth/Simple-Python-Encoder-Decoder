import tkinter as tk
from tkinter import ttk
import random


def get_shift_pattern(shift: int, seed: int, shift_pattern_num: int) -> list:
    shift_pattern = []

    real_shift_pattern_num = max(min(shift_pattern_num, 100), 1)

    for i in range(0, real_shift_pattern_num):
        shift_pattern.append(shift + i)

    rng = random.Random(seed)  # Local RNG instance
    rng.shuffle(shift_pattern)

    return shift_pattern


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


def get_random_charsets(charset: str, shift_pattern: list[int]) -> list:
    random_charsets = []
    for i in shift_pattern:
        rng = random.Random(i)  # Local RNG instance
        new_charset = list(charset)
        rng.shuffle(new_charset)
        random_charsets.append(new_charset)
    return random_charsets


def _code(text: str, charset: str, shift_pattern: list[int], encode: bool):
    result = ""

    # generate a list of charsets
    random_charsets = get_random_charsets(charset, shift_pattern)

    # Encode the text using the shift pattern
    pattern_length = len(shift_pattern)
    for i, char in enumerate(text):
        if char in charset:
            i_shift = i % pattern_length
            shift = shift_pattern[i_shift]

            random_charset: str = random_charsets[i_shift]

            index = random_charset.index(char)

            # Calculate the new index based on encoding or decoding
            offset : int
            if encode:
                offset = (index + shift) % len(random_charset)
            else:
                offset = (index - shift) % len(random_charset)

            # Append the character from the random charset
            result += random_charset[offset]
        else:
            result += char
    return result


def encode(text: str, charset: str, shift_pattern: list[int]) -> str:
    return _code(text, charset, shift_pattern, encode=True)


def decode(text: str, charset: str, shift_pattern: list[int]) -> str:
    return _code(text, charset, shift_pattern, encode=False)


class EncoderDecoderUI():
    def __init__(self, seed: int, shift: int, shift_pattern_num: int):
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

        ttk.Label(self.root, text="ShiftPattern(Max 100):").grid(row=2, column=1, padx=5, sticky="e")
        self.shift_pattern_entry = ttk.Entry(self.root, width=5)
        self.shift_pattern_entry.insert(0, str(shift_pattern_num))
        self.shift_pattern_entry.grid(row=2, column=2, padx=5, sticky="w")

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
            shift_pattern_num = int(self.shift_pattern_entry.get())
            seed = int(self.seed_entry.get())
        except ValueError:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Error: Shift and Seed must be integers.")
        return seed, shift, shift_pattern_num


    def on_encode(self):
        shift, seed, shift_pattern_num = self.get_seed_and_shift()
        charset = generate_charset(seed)
        shift_pattern = get_shift_pattern(shift, seed, shift_pattern_num)
        text = self.input_text.get("1.0", tk.END).rstrip('\n')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, encode(text, charset, shift_pattern))


    def on_decode(self):
        shift, seed, shift_pattern_num = self.get_seed_and_shift()
        charset = generate_charset(seed)
        shift_pattern = get_shift_pattern(shift, seed, shift_pattern_num)
        text = self.input_text.get("1.0", tk.END).rstrip('\n')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, decode(text, charset, shift_pattern))


if __name__ == "__main__":
    EncoderDecoderUI(357, 8, 20)
