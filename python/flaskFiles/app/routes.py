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

@app.route('/')
@app.route('/index')
def index():
    xmldir = 'app/xml/'
    testFileName = 'TEST-SmokeTest.xml'

    testInfo = parsexmlFile(xmldir + testFileName)
    pprint(testInfo)
    return render_template('index.html', title = testFileName, TestInformation = testInfo)

@app.route('/api')
def api():
    allowed = True
    if (allowed): ## TODO: authenticate users before allowing them to do stuff
        id = request.args['id']
        action = request.args['action']
        json = database_actions.dostuff(action, request.args)
        return jsonify(json)
