from datetime import datetime
from app import db

class projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(64), index=True,unique=False)

class testRun(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    project = db.Column(db.Integer, index=True, unique=False)
    date = db.Column(db.DateTime, index=False, unique=False)
#   --`test count` VARCHAR(45) NULL, --can calculate
#   --`Started` VARCHAR(45) NULL, --can calculate
#   --`Failed` VARCHAR(45) NULL, --can calculate
#   --`Errors` VARCHAR(45) NULL, --can calculate
#   --`Ignores` VARCHAR(45) NULL, --can calculate

class test_suite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    testsuite = db.Column(db.String(64))
    project = db.Column(db.Integer, db.ForeignKey('projects.id'))
    runTime = db.Column(db.FLOAT)

class test_names(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(64))
    project = db.Column(db.Integer, db.ForeignKey('projects.id'))

class test_case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test_names.id'))
    test_suite = db.Column(db.Integer, db.ForeignKey('test_suite.id'))
    classname = db.Column(db.String(64))
    time = db.Column(db.FLOAT)
    status = db.Column(db.String(10))
    launched = db.Column(db.DateTime)

class issues(db.Model):
    test = db.Column(db.Integer, db.ForeignKey('test_case.id'))
    output = db.Column(db.TEXT)
    status = db.Column(db.VARCHAR(10))
# CREATE TABLE `test_dashboard_schema`.`errors_and_failures`
# (
#     `test` INT foreign key references (`test_dashboard_schema`.`testcase`),
#     `output` TEXT,
#     `status` VARCHAR(10), --whether the test was an error or a fail
# )









#class TestInfo(db.Model):
    # suiteName = db.Column(db.String(64), primary_key=True)
    # testCase = db.Column(db.String(64), index=True, unique=False)
    # testRunName = db.Column(db.Integer, index=True, unique=False)
    # totalTests = db.Column(db.Integer, index=True, unique=False)
    # numErrors = db.Column(db.Integer, index=True, unique=False)
    # failedTest = db.Column(db.Integer, index=True, unique=False)
    # numSkipped = db.Column(db.Integer, index=True, unique=False)
    # totalDuration = db.Column(db.DateTime, index=True, unique=False)
    # error = db.Column(db.Boolean, index=True, unique=False)
    # fail = db.Column(db.Boolean, index=True, unique=False)
    # skipped = db.Column(db.Boolean, index=True, unique=False)
    # posts = db.relationship('Post', backref='author', lazy='dynamic')

#    def __repr__(self):
#        return '<TestInfo {}>'.format(self.username)
