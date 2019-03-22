from datetime import datetime
from app import db

# CREATE SCHEMA `test_dashboard_schema` ;
#
class projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(64), index=True,unique=False)

# CREATE TABLE `test_dashboard_schema`.`projects`
# (
#   `id` int NOT NULL,
#   `Project_Name` VARCHAR(45) NOT NULL,
#   PRIMARY KEY(`id`),
# );
#
class testRun(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)

# CREATE TABLE `test_dashboard_schema`.`testrun` ( --top level of xml file
#   `ID` INT,
#   `Name` VARCHAR(45) NOT NULL,
#   `Project` int(45) foreign key references(`test_dashboard_schema`.`projects`), --Refers to project that the tests belongs to
#   --`test count` VARCHAR(45) NULL, --can calculate
#   --`Started` VARCHAR(45) NULL, --can calculate
#   --`Failed` VARCHAR(45) NULL, --can calculate
#   --`Errors` VARCHAR(45) NULL, --can calculate
#   --`Ignores` VARCHAR(45) NULL, --can calculate
#   `date` datetime(),
#   PRIMARY KEY (`ID` )
# );
#
# CREATE TABLE `test_dashboard_schema`.`testSuite`
# (
#   `TestSuite` VARCHAR(45), --Refers to run of test
#   `Project` INT fOREIGN KEY REFERENCES (`test_dashboard_schema`.`projects`)
#   `RunTime` FLOAT,
# );
#
# CREATE TABLE `test_dashboard_schema`.`test_names`
# {
#   `ID` INT,
#   `test_name` varchar(45),
#   `project` INT fOREIGN KEY REFERENCES (`test_dashboard_schema`.`projects`);
#   PRIMARY KEY (`ID`)
# }
#
# CREATE TABLE `test_dashboard_schema`.`testcase`
# (
#   `ID`  INT, --Needs to be unique because just about everything else repeats
#   `Test ID` INT foreign key references (`test_dashboard_schema`.`test_names`),
#   `TestSuite` VARCHAR(45) NOT NULL,
#   `classname` VARCHAR(45) NOT NULL,
#   `Time` FLOAT,
#   `status` VARCHAR(10),
#   `Launched` datetime(),
#   PRIMARY KEY (`ID`)
# );
#
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
