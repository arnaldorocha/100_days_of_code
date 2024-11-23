import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Função para alternar o idioma
def switch_language(lang):
    global language
    language = lang
    title_label.config(text=texts[lang]["title"])
    choose_label.config(text=texts[lang]["choose"])
    btn_rock.config(text=texts[lang]["rock"])
    btn_paper.config(text=texts[lang]["paper"])
    btn_scissors.config(text=texts[lang]["scissors"])
    lang_btn.config(text=texts[lang]["switch_lang"])
    result_text.set("")

# Função principal do jogo
def play(choice):
    # Mapeamento de escolhas
    options = ["Rock", "Paper", "Scissors"]
    images = [rock_img, paper_img, scissors_img]

    user_choice = options[choice]
    computer_choice = random.choice(options)

    # Exibe imagens correspondentes
    user_label.config(image=images[choice])
    computer_label.config(image=images[options.index(computer_choice)])

    # Determina o resultado
    if user_choice == computer_choice:
        result = texts[language]["draw"]
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = texts[language]["win"]
    else:
        result = texts[language]["lose"]

    result_text.set(result)

# Configuração de texto para idiomas
texts = {
    "en": {
        "title": "Rock, Paper, Scissors",
        "choose": "Make your choice:",
        "rock": "Rock",
        "paper": "Paper",
        "scissors": "Scissors",
        "switch_lang": "Switch to Portuguese",
        "win": "You Win!",
        "lose": "You Lose!",
        "draw": "It's a Draw!",
    },
    "pt": {
        "title": "Pedra, Papel, Tesoura",
        "choose": "Faça sua escolha:",
        "rock": "Pedra",
        "paper": "Papel",
        "scissors": "Tesoura",
        "switch_lang": "Mudar para Inglês",
        "win": "Você Ganhou!",
        "lose": "Você Perdeu!",
        "draw": "Empate!",
    }
}

# Inicializa a interface
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("600x600")
root.minsize(600, 600)
root.resizable(True, True)
language = "en"

# Carregando imagens
rock_img = ImageTk.PhotoImage(Image.open(r"C:\Users\arnal\OneDrive\Área de Trabalho\Python_Way\workspace\programador_junior\aprendendo\beginner_projects\4_randomisation_list\game_rock_paper_scissors\rock.png").resize((150, 150)))
paper_img = ImageTk.PhotoImage(Image.open(r"C:\Users\arnal\OneDrive\Área de Trabalho\Python_Way\workspace\programador_junior\aprendendo\beginner_projects\4_randomisation_list\game_rock_paper_scissors\paper.png").resize((150, 150)))
scissors_img = ImageTk.PhotoImage(Image.open(r"C:\Users\arnal\OneDrive\Área de Trabalho\Python_Way\workspace\programador_junior\aprendendo\beginner_projects\4_randomisation_list\game_rock_paper_scissors\scissors.png").resize((150, 150)))

# Título
title_label = tk.Label(root, text=texts[language]["title"], font=("Arial", 18, "bold"), bg="#3b5998", fg="white")
title_label.pack(fill="x")

# Escolha do jogador
choose_label = tk.Label(root, text=texts[language]["choose"], font=("Arial", 14))
choose_label.pack(pady=10)

# Resultado do jogo 
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

# Área de imagens
frame = tk.Frame(root)
frame.pack(pady=20)

user_label = tk.Label(frame, image=rock_img)
user_label.grid(row=0, column=0, padx=20)

computer_label = tk.Label(frame, image=rock_img)
computer_label.grid(row=0, column=1, padx=20)

# Botões de escolha
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

btn_rock = tk.Button(button_frame, text=texts[language]["rock"], font=("Arial", 12), command=lambda: play(0))
btn_rock.grid(row=0, column=0, padx=10)

btn_paper = tk.Button(button_frame, text=texts[language]["paper"], font=("Arial", 12), command=lambda: play(1))
btn_paper.grid(row=0, column=1, padx=10)

btn_scissors = tk.Button(button_frame, text=texts[language]["scissors"], font=("Arial", 12), command=lambda: play(2))
btn_scissors.grid(row=0, column=2, padx=10)

# Botão para trocar idioma
lang_btn = tk.Button(root, text=texts[language]["switch_lang"], command=lambda: switch_language("pt" if language == "en" else "en"))
lang_btn.pack(pady=10)

# Inicia a interface
root.mainloop()
