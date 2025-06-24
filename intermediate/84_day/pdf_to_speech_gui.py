import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
import PyPDF2
from gtts import gTTS
import os

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    entry_pdf.delete(0, tk.END)
    entry_pdf.insert(0, filename)

def browse_save_location():
    filepath = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
    if filepath:
        save_path_var.set(filepath)

def toggle_save_location():
    if save_var.get():
        btn_save_location.pack(pady=5)
        entry_save_path.pack(pady=5)
    else:
        btn_save_location.pack_forget()
        entry_save_path.pack_forget()
        save_path_var.set('')

def convert_to_speech():
    pdf_file = entry_pdf.get()
    start_page = int(entry_start.get()) if entry_start.get().isdigit() else 1
    end_page = int(entry_end.get()) if entry_end.get().isdigit() else None
    speed = int(speed_var.get())
    voice_type = voice_var.get()
    save_audio = save_var.get()
    save_path = save_path_var.get()

    if not os.path.isfile(pdf_file):
        messagebox.showerror("Erro", "Arquivo PDF não encontrado!")
        return

    try:
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            text = ''

            if not end_page or end_page > num_pages:
                end_page = num_pages

            for page_num in range(start_page - 1, end_page):
                page = reader.pages[page_num]
                text += page.extract_text()

        if not text.strip():
            messagebox.showwarning("Atenção", "Nenhum texto encontrado no intervalo selecionado.")
            return

        if save_audio:
            if not save_path:
                messagebox.showerror("Erro", "Por favor, escolha o local para salvar o arquivo MP3.")
                return
            tts = gTTS(text=text, lang='pt')
            tts.save(save_path)
            messagebox.showinfo("Sucesso", f"Áudio salvo em: {save_path}")
        else:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            # Seleciona voz
            if voice_type == "Feminina":
                engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
            else:
                engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', speed)
            engine.say(text)
            engine.runAndWait()

    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao processar o PDF:\n{e}")

# Configuração da Janela
root = tk.Tk()
root.title("Conversor PDF para Fala")
root.geometry("500x500")
root.resizable(False, False)

# Campos de entrada
tk.Label(root, text="Arquivo PDF:").pack(pady=5)
entry_pdf = tk.Entry(root, width=60)
entry_pdf.pack()
tk.Button(root, text="Selecionar Arquivo PDF", command=browse_file).pack(pady=5)

frame_pages = tk.Frame(root)
frame_pages.pack(pady=5)
tk.Label(frame_pages, text="Página Inicial:").grid(row=0, column=0, padx=5)
entry_start = tk.Entry(frame_pages, width=5)
entry_start.grid(row=0, column=1, padx=5)
tk.Label(frame_pages, text="Página Final:").grid(row=0, column=2, padx=5)
entry_end = tk.Entry(frame_pages, width=5)
entry_end.grid(row=0, column=3, padx=5)

# Voz
tk.Label(root, text="Tipo de Voz:").pack(pady=5)
voice_var = tk.StringVar(value="Masculina")
tk.Radiobutton(root, text="Masculina", variable=voice_var, value="Masculina").pack()
tk.Radiobutton(root, text="Feminina", variable=voice_var, value="Feminina").pack()

# Velocidade
tk.Label(root, text="Velocidade da Fala (padrão = 200):").pack(pady=5)
speed_var = tk.StringVar(value="200")
tk.Entry(root, textvariable=speed_var, width=10).pack()

# Salvar como MP3
save_var = tk.BooleanVar()
tk.Checkbutton(root, text="Salvar como MP3", variable=save_var, command=toggle_save_location).pack(pady=5)

save_path_var = tk.StringVar()
btn_save_location = tk.Button(root, text="Selecionar Local de Salvamento", command=browse_save_location)
entry_save_path = tk.Entry(root, textvariable=save_path_var, width=60, state='readonly')

# Botão Executar
tk.Button(root, text="Converter", bg="green", fg="white", command=convert_to_speech).pack(pady=10)

root.mainloop()
