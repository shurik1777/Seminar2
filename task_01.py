"""
Задание №2.
Создать страницу с кнопкой "Нажми меня",
при нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index_0.html',
                           title='Стартовая страница')


@app.route('/data')
def data():
    return render_template('data.html',
                           title='Информация')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Приветсвую Вас {name} !'
    return render_template('data.html')


if __name__ == '__main__':
    app.run(debug=True)
