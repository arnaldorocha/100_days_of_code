import tkinter as tk
from tkinter import messagebox
import time
import random

# Lista de frases para o usuário digitar
sentences = [
    "O rápido marrom raposa pula sobre o cão preguiçoso.",
    "Python é uma linguagem de programação poderosa e fácil de aprender.",
    "A prática leva à perfeição.",
    "Velocidade de digitação é uma habilidade útil."
]

# Variável para controlar o tempo de início
start_time = 0

# Função para iniciar o teste
def start_test(event):
    global start_time
    start_time = time.time()  # Salva o tempo quando o usuário começa a digitar

# Função para calcular o resultado
def check_result():
    global start_time
    end_time = time.time()  # Marca o tempo de término
    total_time = end_time - start_time  # Tempo total gasto
    user_input = text_input.get("1.0", tk.END).strip()  # Texto que o usuário digitou
    word_count = len(user_input.split())  # Conta as palavras digitadas
    wpm = (word_count / total_time) * 60  # Calcula palavras por minuto

    # Verificar se o texto está correto
    if user_input == sentence_label.cget("text"):
        messagebox.showinfo("Resultado", f"Parabéns! Sua velocidade foi {wpm:.2f} palavras por minuto.")
    else:
        messagebox.showwarning("Resultado", "O texto digitado não corresponde ao original. Tente novamente!")

# Função para escolher uma nova frase
def reset_test():
    global start_time
    start_time = 0
    new_sentence = random.choice(sentences)  # Escolhe uma frase aleatória
    sentence_label.config(text=new_sentence)  # Atualiza a frase na tela
    text_input.delete("1.0", tk.END)  # Limpa o campo de texto

# Interface Tkinter
root = tk.Tk()
root.title("Typing Speed Test")

# Label com a frase para digitar
sentence_label = tk.Label(root, text=random.choice(sentences), font=("Arial", 14), wraplength=600, justify="center")
sentence_label.pack(pady=20)

# Campo de texto para o usuário digitar
text_input = tk.Text(root, height=5, width=70, font=("Arial", 12))
text_input.pack(pady=10)
text_input.bind('<FocusIn>', start_test)  # Começa a contar o tempo ao focar no campo

# Botão para verificar resultado
check_button = tk.Button(root, text="Verificar Resultado", command=check_result)
check_button.pack(pady=5)

# Botão para reiniciar com nova frase
reset_button = tk.Button(root, text="Nova Frase", command=reset_test)
reset_button.pack(pady=5)

root.mainloop()
