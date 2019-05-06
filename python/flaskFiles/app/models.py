from datetime import datetime
from app import db
#@app.route('/')
#from app.db import db

class projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(64), index=True,unique=False)
    passing = db.Column(db.Integer, index=False, unique=False)
    failing = db.Column(db.Integer, index=False, unique=False)
    didnt_run = db.Column(db.Integer, index=False, unique=False)
    new_fail = db.Column(db.Integer, index=False, unique=False)
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
    runtime = db.Column(db.FLOAT)

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
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.Integer, db.ForeignKey('test_case.id'))
    output = db.Column(db.TEXT)
    status = db.Column(db.VARCHAR(10))
