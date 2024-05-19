"""
Задание №3.
Создать страницу, на которой будет форма для ввода логина
и пароля.
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой если логин и пароль не совпадает.
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

LOGIN = 'admin'
PASSWORD = '123'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index_1.html',
                           title='Стартовая страница')


@app.route('/data')
def data():
    return render_template('data.html',
                           title='Информация')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    get_login = request.form.get('login')
    get_password = request.form.get('password')
    next_page = request.args.get('next')

    if get_login == LOGIN and get_password == PASSWORD:
        if next_page is not None:
            return redirect(next_page)
        else:
            return redirect(url_for('index'))
    else:
        return render_template('error.html',
                               message='Неверный логин или пароль.'
                                       ' Попробуйте еще раз.')


if __name__ == '__main__':
    app.run(debug=True)
