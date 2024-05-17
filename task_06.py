"""
Задание №6.
Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
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
