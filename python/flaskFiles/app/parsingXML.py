#! /usr/bin/python
from xml.dom import minidom
import pprint
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as ElementTree
from app.database_actions import database_actions

def parsexmlFile(testFileName):
    myDoc = minidom.parse(testFileName)

    testSuite = myDoc.getElementsByTagName('testsuite')
    testCases = myDoc.getElementsByTagName('testcase')

    totalTests = testSuite[0].attributes['tests'].value
    numErrors = testSuite[0].attributes['errors'].value
    failedTest = testSuite[0].attributes['failures'].value
    numSkipped = testSuite[0].attributes['skipped'].value

    name = testSuite[0].attributes['name'].value
    totalDuration = testSuite[0].attributes['time'].value
    overallInfo= {}
    suiteInfo = []
    indivTestInfo = []
    testInfo = []

    for elem in testCases:

        time = elem.attributes['time'].value
        error = elem.getElementsByTagName('error')
        failure = elem.getElementsByTagName('failure')
        skipped = elem.getElementsByTagName('skipped')
        className = elem.attributes['classname'].value
        errorBool = False
        failureBool = False
        skippedBool = False
        errorMessage = 'None'
        failureMessage = 'None'
        skippedMessage = 'None'

        if(error != [] and time != 0):
            errorBool = True
            errorMessage = 'Error'
        #root = etree.Element(elem)
#            for log in root.xpath("//error"):
#                print log.text
#            print(error)
        elif(failure != [] and time != 0):
            failureBool = True
            failureMessage = 'Failure'
        #root = etree.Element(elem)
#            for log in root.xpath('.//failure'):
#                print log.text
#            print(failure)
        elif(time == '0'):
            skippedBool = True
            skippedMessage = skipped[0].attributes['message'].value
        #        else:
        #            print("Total runtime is " + time)
        #            print("Success")
        indivTestInfo.append({'time':time})
        indivTestInfo.append({'error': errorBool})
        indivTestInfo.append({'errorMessage': errorMessage})
        indivTestInfo.append({'failure': failureBool})
        indivTestInfo.append({'failureMessage': failureMessage})
        indivTestInfo.append({'ignored': skippedBool})
        indivTestInfo.append({'ignoredMessage': skippedMessage})
        indivTestInfo.append({'className':className})
        indivTestInfo.append({'testName':elem.attributes['name'].value})

        testInfo.append({'Individual Test Information': indivTestInfo})
        indivTestInfo = []
    suiteInfo.append({'suiteName':name,'totalTime':totalDuration,'totalTest':totalTests,'numErrors':numErrors,'failedTest':failedTest,'numSkipped':numSkipped})

    overallInfo.update({'SuiteInfo': suiteInfo})
    overallInfo.update({'Info': testInfo})

    return overallInfo

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    testFileName = 'TEST-SmokeTest.xml'
    xinfo = parsexmlFile('TEST-SmokeTest.xml')
    pp.pprint(xinfo)
