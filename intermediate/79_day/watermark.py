import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark Adder Avançado 💧")

        # Upload de imagem
        tk.Button(root, text="📂 Upload Imagem", command=self.load_image).pack(pady=5)

        # Canvas para mostrar imagem
        self.canvas = tk.Canvas(root, width=500, height=500, bg="gray")
        self.canvas.pack()

        # Campo texto da marca
        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack(pady=5)
        self.text_entry.insert(0, "Digite sua marca d'água...")

        # Escolher cor
        self.color = "#FFFFFF"
        tk.Button(root, text="🎨 Escolher Cor", command=self.choose_color).pack(pady=2)

        # Controle de Opacidade
        tk.Label(root, text="Opacidade (0-255):").pack()
        self.opacity_scale = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
        self.opacity_scale.set(128)
        self.opacity_scale.pack(pady=2)

        # Menu de posição
        tk.Label(root, text="Posição:").pack()
        self.position_var = tk.StringVar(value="Bottom Right")
        positions = ["Top Left", "Top Right", "Center", "Bottom Left", "Bottom Right"]
        tk.OptionMenu(root, self.position_var, *positions).pack()

        # Botão aplicar
        tk.Button(root, text="💧 Adicionar Watermark", command=self.add_watermark).pack(pady=5)

        # Botão salvar
        tk.Button(root, text="💾 Salvar Imagem", command=self.save_image).pack(pady=5)

        self.original_image = None
        self.watermarked_image = None
        self.tk_image = None

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Escolha uma cor")
        if color_code:
            self.color = color_code[1]  # Pega cor hexadecimal

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.original_image = Image.open(file_path).convert("RGBA")
            self.display_image(self.original_image)

    def display_image(self, pil_image):
        image = pil_image.copy()
        image.thumbnail((500, 500))
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.delete("all")
        self.canvas.create_image(250, 250, image=self.tk_image)

    def add_watermark(self):
        if self.original_image:
            image = self.original_image.copy()
            text = self.text_entry.get()
            opacity = self.opacity_scale.get()

            watermark_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(watermark_layer)

            try:
                font = ImageFont.truetype("arial.ttf", 36)
            except:
                font = ImageFont.load_default()

            # Calcula tamanho do texto
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            # Determina posição
            positions = {
                "Top Left": (10, 10),
                "Top Right": (image.width - text_width - 10, 10),
                "Center": ((image.width - text_width) // 2, (image.height - text_height) // 2),
                "Bottom Left": (10, image.height - text_height - 10),
                "Bottom Right": (image.width - text_width - 10, image.height - text_height - 10),
            }
            pos = positions.get(self.position_var.get(), (10, 10))

            # Desenha o texto com a opacidade escolhida
            r, g, b = ImageColor.getrgb(self.color)
            draw.text(pos, text, font=font, fill=(r, g, b, opacity))

            # Combina a marca com a imagem original
            self.watermarked_image = Image.alpha_composite(image, watermark_layer)
            self.display_image(self.watermarked_image)

    def save_image(self):
        if self.watermarked_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG Image", "*.png")])
            if file_path:
                self.watermarked_image.save(file_path)
                print(f"Imagem salva em: {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()