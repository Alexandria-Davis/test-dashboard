#! /usr/bin/python
from xml.dom import minidom
import pprint
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as ElementTree
from database_actions import add_from_file

def parsexmlFile(testFileName):
    myDoc = minidom.parse(testFileName)
    #testRun = myDoc.getElementsByTagName('testrun')
    testSuite = myDoc.getElementsByTagName('testsuite')
    testCases = myDoc.getElementsByTagName('testcase')
    
    totalTests = testSuite[0].attributes['tests'].value
    numErrors = testSuite[0].attributes['errors'].value
    failedTest = testSuite[0].attributes['failures'].value
    numSkipped = testSuite[0].attributes['skipped'].value
    #numIgnored = testSuite[0].attributes['ignored'].value
    
    name = testSuite[0].attributes['name'].value
    totalDuration = testSuite[0].attributes['time'].value
    testInfo = []
    allTestInfo = {}
    
    for elem in testCases:
        testInfo.append({'testName':elem.attributes['name'].value})
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
        testInfo.append({'time':time})
        testInfo.append({'error': errorBool})
        testInfo.append({'failure': failureBool})
        testInfo.append({'ignored': skippedBool})
    allTestInfo.update({'Test Information': testInfo})
    allTestInfo.update({'suiteName':name,'totalTime':totalDuration,'totalTest':totalTests,'numErrors':numErrors,'failedTest':failedTest,'numSkipped':numSkipped})
    
    return allTestInfo

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    testFileName = 'TEST-SmokeTest.xml'
    xinfo = parsexmlFile('TEST-SmokeTest.xml')
    pp.pprint(xinfo)
