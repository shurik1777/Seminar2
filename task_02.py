"""
Задание №2.
Создать страницу, с изображением и ссылкой
на другую страницу, на которой будет отображаться форма
для загрузки изображений.
"""
from flask import Flask, render_template, request
from pathlib import PurePath, Path
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Стартовая страница')


@app.route('/data')
def data():
    return render_template('data.html',
                           title='Информация')


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'static/image',
                                    file_name))
        # Уточнение если не будет создана директория uploads
        # - то будут ошибки не найденных путей
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html',
                           title='Получаем данные')


if __name__ == '__main__':
    app.run(debug=True)
