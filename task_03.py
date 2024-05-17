"""
Задание №3.
Создать страницу, на которой будет форма для ввода логина
и пароля.
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.
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
