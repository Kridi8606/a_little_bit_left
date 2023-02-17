from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def DaDaDa():
    return '''<p><strong>Миссия Колонизация Марса</strong></p>'''


@app.route('/index')
def index():
    return '''<p><strong>И на Марсе будут яблони цвести!</strong></p>'''


@app.route('/promotion')
def promotion():
    return '''
    <p><strong>Человечество вырастает из детства.</strong></p>
    <p><strong>Человечеству мала одна планета.</strong></p>
    <p><strong>Мы сделаем обитаемыми безжизненные пока планеты.</strong></p>
    <p><strong>И начнем с Марса!</strong></p>
    <p><strong>Присоединяйся!</strong></p>
    '''


@app.route('/image_mars')
def image_mars():
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Привет, Марс!</title>
        <link rel="stylesheet" href="https://necolas.github.io/normalize.css/8.0.1/normalize.css ">
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src='{url_for('static', filename='mars.png')}' alt="я не знаю почему оно не выводится, и я устал">
        <p>Вот она какая, Земля через сто лет.</p>
    </body>
    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')