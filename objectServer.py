from datetime import datetime
import glob
import io
import os
import time
from logging import debug

import flask
import numpy as np
from flask import Flask, flash, redirect, render_template, request, url_for
from keras.applications import ResNet50, imagenet_utils
from keras.preprocessing.image import img_to_array
from PIL import Image
from werkzeug.utils import secure_filename

import objectDetection

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
model = None

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/')
def home():
    return flask.render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        file_name, file_extension = os.path.splitext(filename)
        now = datetime.now().strftime('%H%M%S')
        filename = file_name + now + file_extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        img, time_taken = objectDetection.run_detector('static/uploads/' + filename)
        img = Image.fromarray(img, "RGB")
        new_filename = 'temp.jpg'
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded and displayed below')
        flash('Time taken = ' + str(time_taken))
        return render_template('upload.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

# @app.route('/display/temp.jpg')
# def display_modified_image():
#     return redirect(url_for('static', filename='uploads/' + 'temp.jpg'), code=301)

if __name__ == '__main__':
    print(("* Loading Keras model and Flask starting server..."
    "please wait until server has fully started"))
    app.run()
