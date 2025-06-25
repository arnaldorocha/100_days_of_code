import os
from flask import Flask, request, render_template
from PIL import Image
from collections import Counter

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def get_most_common_colors(image_path, num_colors=5):
    with Image.open(image_path) as img:
        img = img.resize((100, 100))  # Reduz para agilizar a contagem
        pixels = list(img.getdata())

        # Remove pixels com transparência, se houver
        pixels = [pixel for pixel in pixels if isinstance(pixel, tuple) and len(pixel) >= 3]

        counter = Counter(pixels)
        most_common = counter.most_common(num_colors)
        return most_common


@app.route('/', methods=['GET', 'POST'])
def index():
    colors = []
    filename = None

    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            colors = get_most_common_colors(filename)

    return render_template('index.html', colors=colors, filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
