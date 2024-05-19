"""
Задание №6.
Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index_5.html',
                           title='Стартовая страница')


@app.route('/data')
def data():
    return render_template('data.html',
                           title='Информация')


@app.route('/check_age', methods=['POST'])
def check_age():
    name = request.form['name']
    age = int(request.form['age'])

    if age >= 18:
        return redirect(url_for('result', name=name, age=age))
    else:
        return redirect(url_for('error'))


@app.route('/result')
def result():
    name = request.args.get('name')
    age = request.args.get('age')
    return f'Привет, {name}! Твой возраст равен {age} или побольше поэтому добро пожаловать!'


@app.route('/error')
def error():
    return 'Ошибка! Ты слишком молод для этого! 🙅‍♂️❌'


if __name__ == '__main__':
    app.run(debug=True)
