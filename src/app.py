from flask import Flask, request, Response, jsonify ,render_template ,redirect, url_for
import json
from werkzeug.utils import secure_filename






UPLOAD_FOLDER = 'helpers/dump/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024