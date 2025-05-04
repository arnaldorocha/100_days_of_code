from tkinter import *
import requests
import os

# Caminho absoluto das imagens baseado na localização do script
current_dir = os.path.dirname(__file__)
image_background = os.path.join(current_dir, "background.png")
image_kanye = os.path.join(current_dir, "kanye.png")


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


# Cria a janela principal
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Cria as imagens (agora que a janela já foi criada)
background_img = PhotoImage(file=image_background)
kanye_img = PhotoImage(file=image_kanye)

# Canvas e elementos gráficos
canvas = Canvas(width=300, height=414)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250,
                                 font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Botão
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
