"""
Задание №4.
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index_0.html',
                           title='Стартовая страница')


if __name__ == '__main__':
    app.run(debug=True)
