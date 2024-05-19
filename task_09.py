"""
Задание №9.
Создать страницу, с формой для ввода имени
и электронной почты, при отправке которых будет создан
cookie файл с данными пользователя также будет произведено
перенаправление на страницу приветствия,
 где будет отображаться имя пользователя.

На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""
from flask import (Flask, render_template,
                   request, make_response,
                   redirect, url_for)

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index_2.html',
                           title='Стартовая страница')


@app.route('/data')
def data():
    return render_template('data.html',
                           title='Информация')


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        response = make_response(render_template('welcome.html', name=name))
        response.set_cookie('user_data', f'name={name}&email={email}')
        return response
    else:
        return render_template('index_2.html')


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    if 'user_data' in request.cookies:
        response.set_cookie('user_data', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
