import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify , render_template ,send_from_directory
from werkzeug.utils import secure_filename
from helpers import generateSmalls as gs

ALLOWED_EXTENSIONS = set([ 'pdf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resp = jsonify({'message' : 'File successfully uploaded'})

		num_groups = request.form.get("num_groups")
		num_pages = request.form.get("num_pages")
		path = gs.generatePdfZip(int(num_groups) , int(num_pages) , app.config['UPLOAD_FOLDER']+  filename)

		
		resp.status_code = 201
		return send_from_directory(path, 'result.zip')
	else:
		resp = jsonify({'message' : 'Allowed file types are  pdf'})
		resp.status_code = 400
		return resp



@app.route('/file-upload')
def preview_upload_page():
   return render_template('upload.html')

if __name__ == "__main__":
	app.run()
	