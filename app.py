from flask import Flask, render_template, redirect, request
import json
# from werkzeug.utils import secure_filename
# from flask_uploads import configure_uploads, IMAGES, UploadSet
from random import randint
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static', 'img')
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gal')
def gal():
    return render_template('gal.html')

@app.route('/arc')
def arc():
    return render_template('arc.html')

@app.route('/galpic')
def galpic():
    return render_template('galpic.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
