CREATE SCHEMA `test_dashboard_schema` ;

CREATE TABLE `test_dashboard_schema`.`projects`
(
  `id` VARCHAR(45) NOT NULL,
  `Project` VARCHAR(45) NOT NULL,
);

CREATE TABLE `test_dashboard_schema`.`testrun` ( --top level of xml file
  `ID` INT,
  `Name` VARCHAR(45) NOT NULL,
  `Project` VARCHAR(45) NULL, --Refers to project that the tests belongs to
  --`test count` VARCHAR(45) NULL, --can calculate
  --`Started` VARCHAR(45) NULL, --can calculate
  --`Failed` VARCHAR(45) NULL, --can calculate
  --`Errors` VARCHAR(45) NULL, --can calculate
  `Ignores` VARCHAR(45) NULL,
  `date` datetime(),
  PRIMARY KEY (`int` )
);

CREATE TABLE `test_dashboard_schema`.`testSuite`
(
  `Test_Name` VARCHAR(45), --Refers to test in test suite
  `TestSuite` VARCHAR(45), --Refers to run of test
  -- `Time` FLOAT,
);

CREATE TABLE `test_dashboard_schema`.`testcase`
(
  `ID`  INT; --Needs to be unique because just about everything else repeats
  `TestSuite` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `classname` VARCHAR(45) NOT NULL,
  `Time` FLOAT,
  `status` VARCHAR(45),
  `Launched` datetime(),
);

CREATE TABLE `test_dashboard_schema`.`errors_and_failures`
(
    `test` VARCHAR(45),
    `output` TEXT,
    `error/fail` boolean, --whether the test was an error or a fail
)
