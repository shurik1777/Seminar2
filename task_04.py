"""
Задание №4.
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index_7.html',
                           title='Стартовая страница')


@app.route('/data')
def data():
    return render_template('data.html',
                           title='Информация')


@app.route('/submit', methods=['POST'])
def submit():
    text = request.form.get('text')
    if text:
        words = text.split()
        count = len(words)
        return redirect(url_for('result', count=count))
    return redirect(url_for('index'))


@app.route('/result/<count>')
def result(count):
    return render_template('result_count.html', count=count)


if __name__ == '__main__':
    app.run(debug=True)
