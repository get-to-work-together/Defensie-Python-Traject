from flask import Flask, render_template, request, jsonify
from html import escape

from models.orakel import geef_wijsheid

namen = ['Peter',
        'Stefan',
        'Bryan',
        'Reinier']

def run():

    app = Flask(__name__,
                template_folder='templates',
                static_url_path='',
                static_folder='static')

    @app.route('/')
    def home():
        return '<p>Hello world! You are on at the Orakel site.</p>'

    @app.route('/info')
    def info():
        return render_template('info.html')

    @app.route('/namen')
    def toon_namen():
        return render_template('namen.html', namen=namen)

    @app.route('/orakel')
    def toon_orakel():
        wijsheid = geef_wijsheid()
        return render_template('wijsheid.html', wijsheid=wijsheid)

    @app.route('/hoi')
    def toon_hoi():
        naam = request.args.get('naam')
        return f'Hoi {naam}.'

    @app.route('/api/v1/orakel')
    def toon_orakel_api():
        wijsheid = geef_wijsheid()
        return jsonify(escape(wijsheid))


    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    run()