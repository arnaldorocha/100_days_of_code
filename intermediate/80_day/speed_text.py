import tkinter as tk
from tkinter import messagebox
import time
import random
import ttkbootstrap as tb
from ttkbootstrap.constants import *

sentences = [
    "A prática leva à perfeição.",
    "Python é uma linguagem poderosa e divertida.",
    "Desafie-se a digitar cada vez mais rápido.",
    "O rápido marrom raposa pula sobre o cão preguiçoso.",
    "A velocidade de digitação é uma habilidade útil."
]

start_time = 0
timer_running = False

def start_timer(event=None):
    global start_time, timer_running
    if not timer_running:
        start_time = time.time()
        timer_running = True
        update_timer()

def update_timer():
    if timer_running:
        elapsed = time.time() - start_time
        timer_label.config(text=f"⏱️ Tempo: {elapsed:.1f} segundos")
        root.after(100, update_timer)  # Atualiza a cada 0,1 segundo

def check_result():
    global timer_running
    timer_running = False
    end_time = time.time()
    total_time = end_time - start_time
    user_text = text_input.get("1.0", tk.END).strip()
    word_count = len(user_text.split())
    wpm = (word_count / total_time) * 60 if total_time > 0 else 0

    if user_text == sentence_label.cget("text"):
        messagebox.showinfo("Resultado", f"✅ Perfeito!\n\n⏱️ Tempo: {total_time:.1f} segundos\n🚀 Velocidade: {wpm:.2f} palavras por minuto")
    else:
        messagebox.showwarning("Resultado", "❌ O texto digitado está incorreto.\n\nTente novamente!")

def reset_test():
    global timer_running
    timer_running = False
    sentence_label.config(text=random.choice(sentences))
    text_input.delete("1.0", tk.END)
    timer_label.config(text="⏱️ Tempo: 0.0 segundos")

root = tb.Window(themename="superhero")
root.title("Typing Speed Test - Tkinter + ttkbootstrap")
root.geometry("700x400")

title_label = tb.Label(root, text="🖥️ Teste de Velocidade de Digitação", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

sentence_label = tb.Label(root, text=random.choice(sentences), font=("Arial", 14), wraplength=650, justify="center")
sentence_label.pack(pady=10)

text_input = tk.Text(root, height=5, width=80, font=("Arial", 12))
text_input.pack(pady=10)
text_input.bind("<FocusIn>", start_timer)

timer_label = tb.Label(root, text="⏱️ Tempo: 0.0 segundos", font=("Arial", 12))
timer_label.pack(pady=5)

button_frame = tb.Frame(root)
button_frame.pack(pady=10)

check_button = tb.Button(button_frame, text="Verificar Resultado ✅", bootstyle=SUCCESS, command=check_result)
check_button.grid(row=0, column=0, padx=10)

reset_button = tb.Button(button_frame, text="Nova Frase 🔄", bootstyle=WARNING, command=reset_test)
reset_button.grid(row=0, column=1, padx=10)

root.mainloop()
