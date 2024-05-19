"""
Задание №5.
Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.
"""
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
#  Без app.secret_key - работать не будет
app.secret_key = '6cfb0f19c1e505e1e715b2ea4622858012176f59f9d21af0ea5fe99825320663'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index_6.html',
                           title='Стартовая страница')


@app.route('/data')
def data():
    return render_template('data.html',
                           title='Информация')


@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    operation = request.form.get('operation')
    if not num1 or not num2 or not operation:
        flash('Все поля должны быть заполнены', 'error')
        return redirect(url_for('index'))
    try:
        if operation == 'add':
            element = int(num1) + int(num2)
        elif operation == 'subtract':
            element = int(num1) - int(num2)
        elif operation == 'multiply':
            element = int(num1) * int(num2)
        elif operation == 'divide':
            element = int(num1) / int(num2)
        return redirect(url_for('result', element=element))
    except ValueError:
        flash('Ошибка: введенные данные не являются числами', 'error')
        return redirect(url_for('index'))


@app.route('/result/<element>')
def result(element):
    return render_template('result.html', element=element)


if __name__ == '__main__':
    app.run(debug=True)
