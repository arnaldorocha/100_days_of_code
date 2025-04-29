# ---------------------------- IMPORTAÇÕES ------------------------------- #
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import threading

# ---------------------------- CONSTANTES ------------------------------- #

# Cores
COR_TRABALHO = "#00b894"      # Verde água
COR_PAUSA_CURTA = "#fdcb6e"   # Amarelo suave
COR_PAUSA_LONGA = "#e17055"   # Laranja queimado
COR_FUNDO = "#f5f6fa"         # Fundo da janela

# Fonte
FONTE_PADRAO = "Arial"

# Tempos em minutos
MINUTOS_TRABALHO = 25
MINUTOS_PAUSA_CURTA = 5
MINUTOS_PAUSA_LONGA = 20

# Caminhos para sons
CAMINHO_SONS = {
    "work": "c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/28_day/my_pomodoro/work.mp3",
    "short_break": "c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/28_day/my_pomodoro/short_break.mp3",
    "long_break": "c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/28_day/my_pomodoro/long_break.mp3"
}

# Variáveis de controle
reps = 0           # Quantas sessões foram feitas
timer = None       # Guarda o after do cronômetro

# ---------------------------- FUNÇÕES PRINCIPAIS ------------------------------- #

def resetar_cronometro():
    """Reseta o cronômetro, progresso e ciclos."""
    window.after_cancel(timer)
    canvas.itemconfig(texto_timer, text="00:00")
    label_titulo.config(text="Pomodoro", fg=COR_TRABALHO)
    label_marcas.config(text="")
    barra_progresso.coords(barra, (0, 0, 0, 20))
    global reps
    reps = 0

def iniciar_cronometro():
    """Começa um novo ciclo Pomodoro."""
    global reps
    reps += 1

    segundos_trabalho = MINUTOS_TRABALHO * 60
    segundos_pausa_curta = MINUTOS_PAUSA_CURTA * 60
    segundos_pausa_longa = MINUTOS_PAUSA_LONGA * 60

    if reps % 8 == 0:
        notificar("Pausa Longa", "Hora de uma pausa longa! 🧘‍♂️", "long_break")
        label_titulo.config(text="Pausa Longa", fg=COR_PAUSA_LONGA)
        contagem_regressiva(segundos_pausa_longa)
    elif reps % 2 == 0:
        notificar("Pausa Curta", "Hora de uma pausa curta! 💧", "short_break")
        label_titulo.config(text="Pausa Curta", fg=COR_PAUSA_CURTA)
        contagem_regressiva(segundos_pausa_curta)
    else:
        notificar("Trabalho", "Vamos focar no trabalho! 💻", "work")
        label_titulo.config(text="Trabalho", fg=COR_TRABALHO)
        contagem_regressiva(segundos_trabalho)

def contagem_regressiva(contagem):
    """Atualiza o cronômetro a cada segundo e controla a barra de progresso."""
    minutos = contagem // 60
    segundos = contagem % 60
    if segundos < 10:
        segundos = f"0{segundos}"

    canvas.itemconfig(texto_timer, text=f"{minutos}:{segundos}")

    # Atualiza a barra de progresso
    tempo_total = (
        MINUTOS_TRABALHO * 60 if reps % 2 != 0 else (MINUTOS_PAUSA_CURTA * 60 if reps % 8 != 0 else MINUTOS_PAUSA_LONGA * 60)
    )
    progresso = (tempo_total - contagem) / tempo_total
    barra_progresso.coords(barra, (0, 0, progresso * 200, 20))

    if contagem > 0:
        global timer
        timer = window.after(1000, contagem_regressiva, contagem - 1)
    else:
        iniciar_cronometro()
        # Atualiza as marcas (✔)
        sessoes_concluidas = reps // 2
        marcas = "✔" * sessoes_concluidas
        label_marcas.config(text=marcas)

def tocar_som(tipo):
    """Toca o som correspondente ao evento."""
    caminho = CAMINHO_SONS.get(tipo)
    if caminho:
        threading.Thread(target=playsound, args=(caminho,), daemon=True).start()

def notificar(titulo, mensagem, tipo_som):
    """Toca o som de alerta e exibe uma notificação."""
    tocar_som(tipo_som)
    messagebox.showinfo(title=titulo, message=mensagem)

# ---------------------------- INTERFACE GRÁFICA ------------------------------- #

# Janela principal
window = Tk()
window.title("Pomodoro Deluxe do Arnaldo 🌟")
window.config(padx=80, pady=40, bg=COR_FUNDO)


# Label de título
label_titulo = Label(text="Pomodoro", fg=COR_TRABALHO, bg=COR_FUNDO, font=(FONTE_PADRAO, 50, "bold"))
label_titulo.grid(column=1, row=0)

# Canvas com a imagem e o cronômetro
canvas = Canvas(width=220, height=224, bg=COR_FUNDO, highlightthickness=0)
imagem_tomate = PhotoImage(file="c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/28_day/pomodoro-start/tomato.png")
canvas.create_image(110, 112, image=imagem_tomate)
texto_timer = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONTE_PADRAO, 35, "bold"))
canvas.grid(column=1, row=1)

# Barra de progresso
barra_progresso = Canvas(width=200, height=20, bg="white", highlightthickness=1, highlightbackground="black")
barra_progresso.grid(column=1, row=2, pady=20)
barra = barra_progresso.create_rectangle(0, 0, 0, 20, fill=COR_TRABALHO)

# Funções de hover nos botões
def on_enter(e, botao, cor):
    botao.config(bg=cor)

def on_leave(e, botao, cor_original):
    botao.config(bg=cor_original)

# Botão Iniciar
botao_iniciar = Button(text="Iniciar", command=iniciar_cronometro, bg=COR_TRABALHO, fg="white", font=(FONTE_PADRAO, 12, "bold"))
botao_iniciar.grid(column=0, row=3)
botao_iniciar.bind("<Enter>", lambda e: on_enter(e, botao_iniciar, "#00a86b"))
botao_iniciar.bind("<Leave>", lambda e: on_leave(e, botao_iniciar, COR_TRABALHO))

# Botão Resetar
botao_resetar = Button(text="Resetar", command=resetar_cronometro, bg=COR_PAUSA_LONGA, fg="white", font=(FONTE_PADRAO, 12, "bold"))
botao_resetar.grid(column=2, row=3)
botao_resetar.bind("<Enter>", lambda e: on_enter(e, botao_resetar, "#d35400"))
botao_resetar.bind("<Leave>", lambda e: on_leave(e, botao_resetar, COR_PAUSA_LONGA))

# Label para mostrar ✔ de progresso
label_marcas = Label(fg=COR_TRABALHO, bg=COR_FUNDO, font=(FONTE_PADRAO, 20))
label_marcas.grid(column=1, row=4)

# Executa a janela
window.mainloop()
