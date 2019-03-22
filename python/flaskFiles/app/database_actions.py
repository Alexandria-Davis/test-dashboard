from app.models import *
from app import db
from pprint import pprint
from xml.dom import minidom
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as ElementTree

class database_actions:
    def __init__():
        return
    def dostuff(action,params):
        json = {"test":"success"}

        if (action == "seed"):
            json.update(database_actions.seed());
        if (action == "get_table"):
            json.update(database_actions.get_table())
        return json
    def getstuff():
        return {"stuff":"gotten"}
    def get_table():
        return {"table":"gotten"}

    def add_from_file(dictionaried):
        print("Parsing file\n\n")
        pprint(dictionaried)
        print("\n\nFile Parsed")
        return 0

    def seed():
        #projects
        project1 = projects(id=None,project_name="testproject1")
        db.session.add(project1)
        project2 = projects(id=None,project_name="testproject2")
        db.session.add(project2)
        #test runs
        testrun1 = testRun(id=None,name="testrun1",project=1,date=None)
        db.session.add(testrun1)
        testrun2 = testRun(id=None,name="testrun2",project=1,date=None)
        db.session.add(testrun2)
        testrun3 = testRun(id=None,name="testrun3",project=2,date=None)
        db.session.add(testrun3)
        testrun4 = testRun(id=None,name="testrun4",project=2,date=None)
        db.session.add(testrun4)
        #test suites
        testsuite1 = test_suite(id=None,testsuite="testsuite1", project=1,runtime=1.1)
        db.session.add(testsuite1)
        testsuite2 = test_suite(id=None,testsuite="testsuite2", project=2,runtime=7.7)
        db.session.add(testsuite2)
        testsuite3 = test_suite(id=None,testsuite="testsuite3", project=2,runtime=1.3)
        db.session.add(testsuite3)
        testsuite4 = test_suite(id=None,testsuite="testsuite4", project=1,runtime=4.35)
        db.session.add(testsuite4)
        #test names
        test1 = test_names(id=None,test_name="test1",project=1)
        db.session.add(test1)
        test2 = test_names(id=None,test_name="test1",project=1)
        db.session.add(test2)
        test3 = test_names(id=None,test_name="test1",project=1)
        db.session.add(test3)
        #test_case
        testcase1 = test_case(id=None, test_id=1, test_suite=1,classname="idk",time=12.2,status="failed",launched=None)
        db.session.add(testcase1)
        #issues
        issue1 = issues(id = 1, test=1, output="Test output. In actuallity this will get very long and very messy. I'm just leaving this here though", status="fail")

        db.session.commit()
        return {"seeded":"true"}

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
