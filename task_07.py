"""
Задание №7.
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
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
