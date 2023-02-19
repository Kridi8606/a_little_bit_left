from flask import Flask, url_for, request

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
        <img src='{url_for('static', filename='img/mars.png')}' alt="я не знаю почему оно не выводится, и я устал">
        <p>Вот она какая, Земля через сто лет.</p>
    </body>
    '''


@app.route('/promotion_image')
def promotion_image():
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Колонизация</title>
        <link rel="stylesheet" href="https://necolas.github.io/normalize.css/8.0.1/normalize.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
        <link rel="stylesheet" href="static/css/style_promotion_image.css">
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src='{url_for('static', filename='img/mars.png')}' alt="я не знаю почему оно не выводится, и я устал">
        <div class="idk" id="id1">
            <strong>Человечество вырастает из детства.</strong>
        </div>
        <div class="idk" id="id2">
            <strong>Человечеству мала одна планета.</strong>
        </div>
        <div class="idk" id="id3">
            <strong>Мы сделаем обитаемыми безжизненные пока планеты.</strong>
        </div>
        <div class="idk" id="id4">
            <strong>И начнём с Марса!</strong>
        </div>
        <div class="idk" id="id5">
            <strong>Присоединяйся!</strong>
        </div>
    </body>
    '''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="last_name" class="form-control" id="last_name" aria-describedby="last_nameHelp" placeholder="Введите фамилию" name="last_name">
                                    <input type="first_name" class="form-control" id="first_name" placeholder="Введите имя" name="first_name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее специальное</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="classSelect">Какие у вас есть профессии?</label>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Пилот</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Строитель</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Врач</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Инженер по терраформированию</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Климатолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Специалист по радиационной защите</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Астрогеолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Гляциолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Инженер жизнеобеспечения</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Оператор марсохода</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Киберинженер</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Штурман</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label" for="acceptRules">Пилот дронов</label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                         </label>
                                       </div>
                                       <div class="form-check">
                                         <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                         <label class="form-check-label" for="female">
                                           Женский
                                         </label>
                                       </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
