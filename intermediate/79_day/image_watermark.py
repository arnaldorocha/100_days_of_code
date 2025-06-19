import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark Adder 🖼️")

        # Botão para carregar imagem
        self.load_button = tk.Button(root, text="📂 Upload Imagem", command=self.load_image)
        self.load_button.pack(pady=10)

        # Canvas para exibir a imagem
        self.canvas = tk.Canvas(root, width=500, height=500, bg="gray")
        self.canvas.pack()

        # Campo para digitar o texto da marca d'água
        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack(pady=5)
        self.text_entry.insert(0, "Digite sua marca d'água...")

        # Botão para adicionar a marca d'água
        self.add_button = tk.Button(root, text="💧 Adicionar Watermark", command=self.add_watermark)
        self.add_button.pack(pady=5)

        # Botão para salvar
        self.save_button = tk.Button(root, text="💾 Salvar Imagem", command=self.save_image)
        self.save_button.pack(pady=5)

        self.original_image = None
        self.watermarked_image = None
        self.tk_image = None

    def load_image(self):
        # Abre um seletor de arquivos para escolher a imagem
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.original_image = Image.open(file_path).convert("RGBA")
            self.display_image(self.original_image)

    def display_image(self, pil_image):
        # Redimensiona para caber no canvas, se necessário
        max_size = (500, 500)
        image = pil_image.copy()
        image.thumbnail(max_size)

        # Converte para Tkinter
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.delete("all")
        self.canvas.create_image(250, 250, image=self.tk_image)

    def add_watermark(self):
        if self.original_image:
            text = self.text_entry.get()
            image = self.original_image.copy()
            drawable = ImageDraw.Draw(image)

            # Escolhe uma fonte simples
            try:
                font = ImageFont.truetype("arial.ttf", 36)
            except:
                font = ImageFont.load_default()

            # Calcula tamanho do texto (usando textbbox, já que textsize foi removido nas versões novas do Pillow)
            bbox = drawable.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            # Define posição (canto inferior direito)
            x = image.width - text_width - 10
            y = image.height - text_height - 10

            # Adiciona o texto com transparência
            drawable.text((x, y), text, font=font, fill=(255, 255, 255, 128))

            self.watermarked_image = image
            self.display_image(image)

    def save_image(self):
        if self.watermarked_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG Image", "*.png")])
            if save_path:
                self.watermarked_image.save(save_path)
                print(f"Imagem salva em: {save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)    
    root.mainloop()
