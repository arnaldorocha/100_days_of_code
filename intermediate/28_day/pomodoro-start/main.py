# Importa tudo do módulo tkinter, que é usado para criar interfaces gráficas
from tkinter import *  

# ---------------------------- CONSTANTS ------------------------------- #
# Definição de cores e fonte para estilizar a interface
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Definição dos tempos (em minutos) para cada fase do Pomodoro
WORK_MIN = 25         # Tempo de trabalho
SHORT_BREAK_MIN = 5   # Tempo de pausa curta
LONG_BREAK_MIN = 20   # Tempo de pausa longa

# Variável global para controlar quantas sessões já passaram
reps = 0
timer = None  # Variável que guardará a referência do método after para cancelar o cronômetro se necessário

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Reseta o cronômetro para o estado inicial."""
    window.after_cancel(timer)  # Cancela o temporizador atual
    canvas.itemconfig(timer_text, text="00:00")  # Reseta o texto para 00:00
    title_label.config(text="Timer")  # Altera o título para 'Timer'
    check_marks.config(text="")  # Limpa os 'check marks'
    global reps
    reps = 0  # Reseta o número de repetições

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Inicia o ciclo de trabalho/pausa baseado nas repetições."""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60          # Converte minutos para segundos
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # A cada 8 sessões, faz uma pausa longa
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        # A cada 2 sessões, faz uma pausa curta
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        # Caso contrário, sessão de trabalho
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Atualiza o cronômetro a cada segundo."""
    count_min = count // 60  # Calcula minutos
    count_sec = count % 60   # Calcula segundos

    # Formata os segundos para sempre ter dois dígitos
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Atualiza o texto do cronômetro na tela
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # Continua o countdown chamando a si mesmo após 1 segundo
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # Quando o tempo acaba, inicia o próximo ciclo
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

# Criação da janela principal
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Criação do título
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Criação do canvas (área onde vai ficar a imagem do tomate e o cronômetro)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/28_day/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Botão de start (iniciar)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Botão de reset (reiniciar)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Label para exibir "check marks" a cada sessão completa
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
check_marks.grid(column=1, row=3)

# Mantém a janela aberta
window.mainloop()
