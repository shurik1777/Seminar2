"""
Задание №8.
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
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
