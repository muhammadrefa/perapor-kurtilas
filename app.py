import sys
import os

from flask import Flask, render_template, request

# from controllers import routes

from controllers.kurtilas_controller import kurtilas
from controllers.siswa_controller import siswa
from controllers.mapel_controller import mapel

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)

app.register_blueprint(kurtilas)
app.register_blueprint(siswa)
app.register_blueprint(mapel)

config = {
    'host'  : "0.0.0.0",
    'port'  : 12345,
    'debug' : False
}

def readConfig():
    f = open('config.txt', 'r')
    for line in f.read().splitlines():
        data = line.split("=")
        config[data[0]] = data[1]
    f.close()


@app.route('/')
def bootstrap():
    return render_template('base/base_content.html')


if __name__ == "__main__":
    readConfig()
    app.run(host=config['host'], port=config['port'], debug=int(config['debug']))
