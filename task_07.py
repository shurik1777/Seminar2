"""
Задание №7.
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index_4.html',
                           title='Стартовая страница')


@app.route('/data')
def data():
    return render_template('data.html',
                           title='Информация')


@app.route('/submit', methods=['POST'])
def submit():
    number = request.form.get('number')
    if number:
        element = f"Число: {number}, Квадрат числа: {int(number) ** 2}"
        return redirect(url_for('result', element=element))
    return redirect(url_for('index'))


@app.route('/result/<element>')
def result(element):
    return render_template('result.html', element=element)


if __name__ == '__main__':
    app.run(debug=True)
