import tkinter as tk
import random

# List of Thai consonants with their names
THAI_CONSONANTS = [
    ("ก", "ก ไก่ (gor kai)"),
    ("\u0e02", "ข ไข่ (kho khai)"),
    ("\u0e03", "ฃ ขวด (kho khuat)"),
    ("\u0e04", "ค ควาย (kho khwai)"),
    ("\u0e05", "ฅ คน (kho khon)"),
    ("\u0e06", "ฆ ระฆัง (kho rakhang)"),
    ("\u0e07", "ง งู (ngo ngu)"),
    ("\u0e08", "จ จาน (cho chan)"),
    ("\u0e09", "ฉ ฉิ่ง (cho ching)"),
    ("\u0e0a", "ช ช้าง (cho chang)")
]


class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")

        self.card_frame = tk.Frame(root, width=300, height=200)
        self.card_frame.pack(pady=20)

        self.label = tk.Label(self.card_frame, text="", font=("Arial", 50))
        self.label.pack()

        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(pady=10)

        self.current_card = None
        self.showing_name = False
        self.next_card()

    def next_card(self):
        self.current_card = random.choice(THAI_CONSONANTS)
        self.label.config(text=self.current_card[0])
        self.showing_name = False

    def flip_card(self):
        if self.showing_name:
            self.label.config(text=self.current_card[0])
        else:
            self.label.config(text=self.current_card[1])
        self.showing_name = not self.showing_name


if __name__ == "__main__":
    root = tk.Tk()
    game = FlashcardGame(root)
    root.mainloop()
