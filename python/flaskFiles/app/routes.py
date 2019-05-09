#!/usr/bin/env python
from flask import render_template
from flask import jsonify
from flask import request
from xml.dom import minidom
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as ElementTree
from app import app
from app.database_actions import database_actions
from app.parsingXML import parsexmlFile
from pprint import pprint
from werkzeug.utils import secure_filename
import os

def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'xml'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        proj = request.form["project"]
        files = request.files.getlist('file[]')
        processed = {}
        for file in files:
            try:
                if file.filename == '':
                     pass;
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    testInfo = parsexmlFile(f"{app.config['UPLOAD_FOLDER']}{filename}")
                    database_actions.add_from_file(testInfo, project=proj)
                    processed[filename] = True
            except Exception as e:
                    processed[filename] = False
        responce = jsonify(processed)
        responce.headers.add("Access-Control-Allow-Origin", "*")
        responce.headers.add("Access-Control-Allow-Headers", "*")
        responce.headers.add("Access-Control-Allow-Methods", "*")
        return responce
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <label for="project">Project</label><br/><br/>
      <input type="text" name="project">
      <br/><br/>
      <label for="file">Upload file:</label><br/><br/>
      <input type="file" name="file[]" multiple>
      <input type=submit value=Upload>
    </form>
    '''
@app.route('/api')
def api():
    allowed = True
    if (allowed): ## TODO: authenticate users before allowing them to do stuff
        action = request.args['action']
        json = database_actions.dostuff(action, request.args)
        resp = jsonify(json)
        resp.headers.add("Access-Control-Allow-Origin", "*")
        resp.headers.add("Access-Control-Allow-Headers", "*")
        resp.headers.add("Access-Control-Allow-Methods", "*")
        return resp;
