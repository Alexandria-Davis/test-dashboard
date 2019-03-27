from flask import render_template
from flask import jsonify
from flask import request
from xml.dom import minidom
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as ElementTree
from app import app
from app.database_actions import database_actions
from pprint import pprint

@app.route('/')
@app.route('/TEST-SmokeTest.xml')
@app.route('/index')
def index():
    xmldir = 'app/xml/'
    testFileName = 'TEST-SmokeTest.xml'
    testSuite = ''
    testCases = ''
    testRunName = ''
    totalTests = ''
    numErrors = ''
    failedTest = ''
    numSkipped = ''
    testName = ''

    parsexmlFile(xmldir + testFileName)
    return render_template('index.html', title = testFileName, TestInfomation = testName)

@app.route('/api')
def api():
    allowed = True
    if (allowed): ## TODO: authenticate users before allowing them to do stuff
        action = request.args['action']
        json = database_actions.dostuff(action, request.args)
        return jsonify(json)




def parsexmlFile(testFileName):
    myDoc = minidom.parse(testFileName)
    #testRun = myDoc.getElementsByTagName('testrun')
    testSuite = myDoc.getElementsByTagName('testsuite')
    testCases = myDoc.getElementsByTagName('testcase')

    testRunName = testSuite[0].attributes['name']
    totalTests = testSuite[0].attributes['tests'].value
    numErrors = testSuite[0].attributes['errors'].value
    failedTest = testSuite[0].attributes['failures'].value
    numSkipped = testSuite[0].attributes['skipped'].value
    #numIgnored = testSuite[0].attributes['ignored'].value

    name = testSuite[0].attributes['name'].value
    totalDuration = testSuite[0].attributes['time'].value
    testInfo = {}
    testName = {}
    for elem in testCases:
        testName.update({'testName':elem.attributes['name'].value})
        #print('Test case name: ' + testName)
        time = elem.attributes['time'].value
        error = elem.getElementsByTagName('error')
        failure = elem.getElementsByTagName('failure')
        errorBool = False
        failureBool = False
        skippedBool = False

        if(error != [] and time != 0):
            errorBool = True
            #root = etree.Element(elem)
            #for log in root.xpath("//error"):
            #print log.text
            print(error)
        elif(failure != [] and time != 0):
            failureBool = True
            #root = etree.Element(elem)
            #for log in root.xpath("//failure"):
            #print log.text
            print(failure)
        elif(time == '0'):
            skippedBool = True
        #        else:
        #            print("Total runtime is " + time)
        #            print("Success")
        testInfo.update({'time':time})
        testInfo.update({'error': errorBool})
        testInfo.update({'failure': failureBool})
        testInfo.update({'ignored': skippedBool})
    testName.update({'Test Information': testInfo})
