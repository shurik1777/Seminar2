"""
Задание №8.
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
"""
from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
#  Без app.secret_key - работать не будет
app.secret_key = '6cfb0f19c1e505e1e715b2ea4622858012176f59f9d21af0ea5fe99825320663'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index_3.html',
                           title='Стартовая страница')


@app.route('/data')
def data():
    return render_template('data.html',
                           title='Информация')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    if name:
        flash(f'Привет, {name}!')
    return redirect(url_for('message'))


@app.route('/message')
def message():
    return render_template('message.html')


if __name__ == '__main__':
    app.run(debug=True)
