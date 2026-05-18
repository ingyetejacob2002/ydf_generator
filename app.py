from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    image_path = None

    if request.method == 'POST':
        name = request.form.get('name')

        file = request.files.get('photo')

        if file and file.filename != '':
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)

            image_path = f'uploads/{filename}'

    return render_template(
        'index.html',
        name=name,
        image_path=image_path
    )


if __name__ == '__main__':
    app.run(debug=True)