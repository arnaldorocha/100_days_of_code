# Importa todos os recursos da biblioteca Tkinter (interface gráfica)
from tkinter import *
# Importa apenas a caixa de mensagem da Tkinter para exibir alertas e informações
from tkinter import messagebox
# Importa a biblioteca 'random' para gerar senhas aleatórias
import random
# Importa pyperclip para copiar a senha gerada para a área de transferência
import pyperclip
# Importa json para salvar e ler dados de um arquivo JSON
import json

# ---------------------------- CONSTANTS ------------------------------- #
# Caminho da imagem do logo do app
LOGO_PATH = "c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/29_day/my_password_manager/logo.png"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Gera listas de caracteres: letras minúsculas, maiúsculas, números e símbolos
    letters = [chr(i) for i in range(97, 123)]      # a-z
    letters_m = [chr(i) for i in range(65, 91)]     # A-Z
    numbers = [str(i) for i in range(0, 10)]        # 0-9
    symbols = ''.join(chr(i) for i in range(33, 48)) + \
              ''.join(chr(i) for i in range(58, 65)) + \
              ''.join(chr(i) for i in range(91, 97)) + \
              ''.join(chr(i) for i in range(123, 127))  # símbolos especiais

    password = []
    # Escolhe aleatoriamente 4 letras minúsculas, 4 maiúsculas, 2 símbolos e 2 números
    password += random.choices(letters, k=4)
    password += random.choices(letters_m, k=4)
    password += random.choices(symbols, k=2)
    password += random.choices(numbers, k=2)
    random.shuffle(password)  # Embaralha a lista

    final_password = ''.join(password)  # Concatena todos os caracteres

    # Atualiza o campo de senha na interface com a senha gerada
    password_entry.delete(0, END)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)  # Copia a senha para a área de transferência

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # Captura os dados inseridos nos campos da interface
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Estrutura os dados para salvar
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Verifica se os campos obrigatórios estão preenchidos
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            # Tenta abrir o arquivo existente
            with open("data.json", "r") as file:
                data = json.load(file)  # Lê o conteúdo existente
        except FileNotFoundError:
            data = {}  # Se o arquivo não existir, cria um dicionário vazio

        data.update(new_data)  # Atualiza os dados existentes com os novos

        # Escreve os dados atualizados de volta no arquivo
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        # Limpa os campos da interface
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- VIEW ALL PASSWORDS ------------------------------- #
def show_all_passwords():
    try:
        # Tenta abrir e ler os dados do arquivo
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        # Se não houver dados, exibe uma mensagem
        messagebox.showinfo(title="No Data", message="No passwords stored yet.")
        return

    # Cria uma nova janela para exibir os dados
    top = Toplevel(window)
    top.title("Stored Passwords")
    top.geometry("450x400")
    top.config(padx=20, pady=20)

    # Adiciona uma barra de rolagem
    scrollbar = Scrollbar(top)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Campo de texto com rolagem para exibir os dados
    text = Text(top, wrap=WORD, yscrollcommand=scrollbar.set)

    # Insere cada conjunto de dados (website, email, senha)
    for website, info in data.items():
        text.insert(END, f"🌐 Website: {website}\n")
        text.insert(END, f"📧 Email: {info['email']}\n")
        text.insert(END, f"🔐 Password: {info['password']}\n")
        text.insert(END, "-"*40 + "\n")

    text.pack(expand=True, fill=BOTH)
    scrollbar.config(command=text.yview)  # Conecta a barra de rolagem ao campo de texto

# ---------------------------- UI SETUP ------------------------------- #
# Cria a janela principal
window = Tk()
window.title("Password Manager")  # Título da janela
window.config(padx=50, pady=50)   # Espaçamento interno (padding)

# Adiciona o logo no topo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=LOGO_PATH)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels (rótulos)
Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

# Campos de entrada (input)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # Coloca o cursor automaticamente nesse campo

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "arnaldorochafilho@gmail.com")  # Preenche com email padrão

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Botões
Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
Button(text="Add", width=36, command=save_password).grid(row=4, column=1, columnspan=2)
Button(text="Show All", width=36, command=show_all_passwords).grid(row=5, column=1, columnspan=2)

# Inicia o loop da interface gráfica
window.mainloop()
