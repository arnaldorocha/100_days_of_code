import tkinter as tk
from tkinter import PhotoImage
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ---------- LER DADOS ---------- #
try:
    data = pd.read_csv("words.csv")
except FileNotFoundError:
    print("Arquivo 'words.csv' não encontrado.")
    exit()

to_learn = data.to_dict(orient="records")

# ---------- FUNÇÕES ---------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_bg, image=card_front_img)
    canvas.itemconfig(card_title, text="Inglês", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_bg, image=card_back_img)
    canvas.itemconfig(card_title, text="Português", fill="white")
    canvas.itemconfig(card_word, text=current_card["Portuguese"], fill="white")

def is_known():
    to_learn.remove(current_card)
    next_card()

# ---------- UI ---------- #
window = tk.Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="right.png")
wrong_img = PhotoImage(file="wrong.png")

right_button = tk.Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()
window.mainloop()
