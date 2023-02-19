from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def DaDaDa():
    with open('html/first_page.html', 'r', encoding='utf-8') as f:
        return f.read()


@app.route('/index')
def index():
    with open('html/index.html', 'r', encoding='utf-8') as f:
        return f.read()


@app.route('/promotion')
def promotion():
    with open('html/promotion.html', 'r', encoding='utf-8') as f:
        return f.read()


@app.route('/image_mars')
def image_mars():
    with open('html/image_mars.html', 'r', encoding='utf-8') as f:
        return f.read().replace('{{ mars_image }}', url_for('static', filename='img/mars.png'))


@app.route('/promotion_image')
def promotion_image():
    with open('html/promotion_image.html', 'r', encoding='utf-8') as f:
        return f.read().replace('{{ mars_image }}', url_for('static', filename='img/mars.png'))


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        with open('html/form_sample.html', 'r', encoding='utf-8') as f:
            return f.read().replace('{{ form.css }}', url_for('static', filename='css/form.css'))
    elif request.method == 'POST':
        print(request.form)
        return "Форма отправлена"


@app.route('/choice/<planets_name>')
def greeting(planets_name):
    planets_name = planets_name.lower()
    text = [planets_name.capitalize(), ]
    if planets_name == 'меркурий':
        text.append('Самая маленькая и самая близкая к Солнцу планета;')
        text.append('Первые люди наблюдали Меркурий невооруженным взглядом примерно 5 тысяч лет назад;')
        text.append('Запущенный в 2004 году зонд «Мессенджер» до сих пор работает на меркурианской орбите;')
        text.append('У Меркурия есть магнитное поле, правда, очень слабое — примерно в сто раз слабее земного;')
        text.append('За меркурианский год планета поворачивается вокруг своей оси на полтора оборота. То есть в течение 2 лет на планете проходит всего лишь трое суток.')
    elif planets_name == 'венера':
        text.append('Вторая по счёту планета;')
        text.append('Самая горячая планета Солнечной системы;')
        text.append('Венеру можно легко увидеть с Земли невооружённым взглядом;')
        text.append('У Венеры и Земли похожие размеры и масса;')
        text.append('Венера имеет очень плотную атмосферу, ее масса в 93 раза больше земного воздуха.')
    elif planets_name == 'марс':
        text.append('Эта планета близкая к Земле;')
        text.append('На ней много необходимых ресурсов;')
        text.append('На ней есть вода и атмосфера;')
        text.append('На ней есть небольшое магнитное поле;')
        text.append('Наконец, она просто красивая!')
    elif planets_name == 'юпитер':
        text.append('Самая большая планета солнечной системы;')
        text.append('Еcли бы Юпитepу удaлocь зaxвaтить в 80 paз бoльшe мaccы, чeм eгo нынeшняя мacca, oн фaктичecки oкaзaлcя бы звeздoй, a нe плaнeтoй;')
        text.append('Aтмocфepa Юпитepa oчeнь пoxoжa нa aтмocфepу нaшeгo Coлнцa;')
        text.append('Oн coвepшaeт oдин oбopoт вoкpуг cвoeй ocи вceгo зa 10 чacoв;')
        text.append('Maгнитнoe пoлe Юпитepa в 20 000 paз cильнee мaгнитнoгo пoля Зeмли.')
    elif planets_name == 'сатурн':
        text.append('ЛЮДИ УЗНАЮТ,')
        text.append('ЧТО СО СМЕРТЬЮ ИХ МИРСКОГО ДУХА')
        text.append('ОНИ ВОЗРОДЯТСЯ В ЕДИНСТВО')
        text.append('КАК БОЛЕЕ СИЛЬНОЕ')
        text.append('БЕСКОНЕЧНОЕ ОБЩЕСТВО.')
    elif planets_name == 'уран':
        text.append('Седьмая по счёту планета;')
        text.append('Этa плaнeтa имeeт нeoбычный cинe-зeлeный цвeт, peзультaтoм кoтopoгo являeтcя пpиcутcтвиe в избыткe мeтaнa в вoдopoднo-гeлиeвoй aтмocфepe плaнeты;')
        text.append('Чтo кacaeтcя мaccы плaнeты, тo 25% зaнимaют кaмни, 5-15% - гeлий и вoдopoд, a 60-70% - лeд;')
        text.append('Уpaн дocтaтoчнo яpкий, чтoбы быть увидeнным чeлoвeкoм;')
        text.append('Этa плaнeтa нa caмoм дeлe являeтcя caмoй xoлoднoй плaнeтoй в Coлнeчнoй cиcтeмe.')
    elif planets_name == 'нептун':
        text.append('Самая дальняя от солнца планета;')
        text.append('На планете дуют самые сильные в Солнечной системе ветра;')
        text.append('Излучает в 2,6 раза больше тепла, чем получает от Солнца;')
        text.append('Я незнаю что писать;')
        text.append('Да и так уже много чего написал.')
    elif planets_name == 'земля':
        text.append('Ахахаха!')
        text.append('Я пошутил!')
        text.append('Вы и так уже здесь.')
        text.append('Бадумс...')
        text.append('Ладно...')
    else:
        text.append('Такого')
        text.append('я')
        text.append('не')
        text.append('ожидал.')
        text.append('GGWPGLHF')
    with open('html/choice.html', 'r', encoding='utf-8') as f:
        f = f.read().replace('{{ choice.css }}', url_for('static', filename='css/choice.css'))
        for i in range(len(text)):
            f = f.replace('{{ text' + str(i) + ' }}', text[i])
        return f


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
