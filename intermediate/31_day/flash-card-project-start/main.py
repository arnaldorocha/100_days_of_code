import tkinter as tk
from tkinter import PhotoImage, messagebox
import pandas as pd
import random
import csv
from pathlib import Path

# Caminho correto
DATA_PATH = Path("c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/31_day/flash-card-project-start")

# Caminho da imagem e CSV
IMAGE_PATH = DATA_PATH / "images"
CSV_PATH = DATA_PATH / "data" / "english_words.csv"

# Diretório onde o CSV será salvo
OUTPUT_PATH = DATA_PATH / "words_learned.csv"

# Verifique se o diretório existe
if not DATA_PATH.exists():
    print(f"Erro: O diretório {DATA_PATH} não existe.")
else:
    print(f"Diretório encontrado: {DATA_PATH}")

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = []
learned_words = []

# ---------- LER DADOS ---------- #
try:
    data = pd.read_csv(CSV_PATH)
    to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    print("Arquivo 'english_words.csv' não encontrado.")
    exit()

# ---------- FUNÇÕES ---------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_bg, image=card_front_img)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["Inglês"], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_bg, image=card_back_img)
    canvas.itemconfig(card_title, text="Portuguese", fill="white")
    canvas.itemconfig(card_word, text=current_card["Português"], fill="white")

def is_known():
    learned_words.append(current_card)
    to_learn.remove(current_card)
    next_card()

def on_closing():
    if learned_words:
        try:
            # Confirmar o salvamento
            with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["Português", "Inglês"])
                writer.writeheader()
                writer.writerows(learned_words)
            messagebox.showinfo("Sucesso", f"{len(learned_words)} palavras foram salvas em {OUTPUT_PATH}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar CSV: {e}")
    else:
        messagebox.showinfo("Sem progresso", "Nenhuma palavra foi aprendida ainda.")
    window.destroy()

# ---------- UI ---------- #

window = tk.Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = tk.Canvas(width=800, height=526) #ajuste tamanho
card_front_img = PhotoImage(file=IMAGE_PATH / "card_front.png")
card_back_img = PhotoImage(file=IMAGE_PATH / "card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file=IMAGE_PATH / "right.png")
wrong_img = PhotoImage(file=IMAGE_PATH / "wrong.png")

right_button = tk.Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# Carregar a primeira carta
next_card()
window.protocol("WM_DELETE_WINDOW", on_closing)  # Fechar com segurança
window.mainloop()
