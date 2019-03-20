#! /usr/bin/python
from xml.dom import minidom
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as ElementTree
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def dataInfo():
    return render_template("/index.html")
app.run()


skipped = False
errors = False
failed = False
#Open up xml file and get ready to parse
myDoc = minidom.parse('TEST-SmokeTest.xml')

#Get elements with tags 'Testsuite' and 'Testcase'
testSuite = myDoc.getElementsByTagName('testsuite')
testCases = myDoc.getElementsByTagName('testcase')

#Get overall information of the test from TestSuite
testRunName = testSuite[0].attributes['name']
totalTests = testSuite[0].attributes['tests'].value
numErrors = testSuite[0].attributes['errors'].value
failedTest = testSuite[0].attributes['failures'].value
numSkipped = testSuite[0].attributes['skipped'].value
name = testSuite[0].attributes['name'].value
totalDuration = testSuite[0].attributes['time'].value


for elem in testCases:
    testName = elem.attributes['name'].value
    time = elem.attributes['time'].value
    if(time == '0'):
        skipped = True
    else:
        print("Total time of "+ testName +" is " + time)
    error = elem.getElementsByTagName('error')
    failure = elem.getElementsByTagName('failure')
    if(error != [] and skipped == False):
        print(error)
    elif(failure != [] and skipped == False):
        print(failure)
    else:
        print("Success")
