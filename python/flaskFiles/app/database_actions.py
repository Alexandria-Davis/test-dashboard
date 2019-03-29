from app.models import *
from app import db
from pprint import pprint
import datetime
class database_actions:
    def __init__():
        return
    def dostuff(action,params):
        json = {}
        if (action == "seed"):
            json.update(database_actions.seed());
        if (action == "get_table"):
            json.update(database_actions.get_table())
        if (action == "query_tests"):
            json.update(database_actions.get_tests_for_project(params["Project_id"]))
        if (action == "query_projects"):
            json.update(database_actions.get_projects())
        return json


    def get_tests_for_project(proj_id):
        q = db.session.query(test_names, test_case).outerjoin(test_case).filter(
        test_names.project == proj_id,
        #test_case.test_id == test_names.id
        )
        q.add_columns('test_names.test_name', 'test_case.time', 'test_case.launched' 'test_case.test_id', 'test_case.id', 'test_case.status')

        v = q.all()
        results = [];
        for i in v:
            if i.test_case is None:
                results.append({
                    "name":i.test_names.test_name,
                    "time":None,
                    "test_name_id":None,
                    "test_id":None,
                    "status":None,
                    "last_run":None
                })
            else:
                results.append({
                    "name":i.test_names.test_name,
                    "time":i.test_case.time,
                    "test_name_id":i.test_case.test_id,
                    "test_id":i.test_case.id,
                    "status":i.test_case.status,
                    "last_run":i.test_case.launched
                })

        return {"Project:": proj_id, "results": results}
    def get_table():
        return {"table":"gotten"}
    def get_projects():
        q = db.session.query(projects)
        q.add_columns('id','project_name')
        v = q.all()
        results = []
        for i in v:
            results.append({"id":i.id,"name":i.project_name})
        return {
            "results":results
        }

    def add_from_file(dictionaried):
        print("Parsing file\n\n")
        pprint(dictionaried)
        print("\n\nFile Parsed")
        return 0

    def seed():
        try:
            #projects
            project1 = projects(id=1,project_name="testproject1")
            db.session.add(project1)
            project2 = projects(id=None,project_name="testproject2")
            db.session.add(project2)
            db.session.commit()
            #test runs
            testrun1 = testRun(id=1,name="testrun1",project=1,date=None)
            db.session.add(testrun1)
            testrun2 = testRun(id=None,name="testrun2",project=1,date=None)
            db.session.add(testrun2)
            testrun3 = testRun(id=None,name="testrun3",project=2,date=None)
            db.session.add(testrun3)
            testrun4 = testRun(id=None,name="testrun4",project=2,date=None)
            db.session.add(testrun4)
            db.session.commit()
            #test suites
            testsuite1 = test_suite(id=1,testsuite="testsuite1", project=1,runtime=1.1)
            db.session.add(testsuite1)
            testsuite2 = test_suite(id=None,testsuite="testsuite2", project=2,runtime=7.7)
            db.session.add(testsuite2)
            testsuite3 = test_suite(id=None,testsuite="testsuite3", project=2,runtime=1.3)
            db.session.add(testsuite3)
            testsuite4 = test_suite(id=None,testsuite="testsuite4", project=1,runtime=4.35)
            db.session.add(testsuite4)
            db.session.commit()
            #test names
            test1 = test_names(id=1,test_name="test1.1",project=1)
            db.session.add(test1)
            test2 = test_names(id=None,test_name="test1.2",project=1)
            db.session.add(test2)
            test3 = test_names(id=None,test_name="test2.1",project=2)
            db.session.add(test3)
            test4 = test_names(id=None,test_name="test2.2",project=2)
            db.session.add(test4)
            db.session.commit()
            #test_case
            testcase1 = test_case(id=1, test_id=1, test_suite=1,classname="idk",time=12.2,status="failed",launched=datetime.datetime.today())
            db.session.add(testcase1)
            testcase2 = test_case(id=None, test_id=1, test_suite=1,classname="idk",time=13.2,status="passed",launched=datetime.datetime.today())
            db.session.add(testcase2)
            testcase3 = test_case(id=None, test_id=2, test_suite=1,classname="idk",time=13.2,status="passed",launched=datetime.datetime.today())
            db.session.add(testcase3)
            testcase4 = test_case(id=None, test_id=3, test_suite=1,classname="idk",time=13.2,status="passed",launched=datetime.datetime.today())
            db.session.add(testcase4)
            testcase5 = test_case(id=None, test_id=4, test_suite=1,classname="idk",time=13.2,status="passed",launched=datetime.datetime.today())
            db.session.add(testcase5)
            db.session.commit()
            #issues
            issue1 = issues(id = 1, test=1, output="Test output. In actuallity this will get very long and very messy. I'm just leaving this here though", status="fail")
            db.session.commit()
            return {"seeded":"true"}
        except Exception as e:
            print(e)
            # TODO: Handle error based on error contents
            return {"seeded": "Error" }
            raise
