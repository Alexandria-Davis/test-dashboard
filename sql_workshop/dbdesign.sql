CREATE SCHEMA `test_dashboard_schema` ;

CREATE TABLE `test_dashboard_schema`.`projects`
(
  `id` int NOT NULL,
  `Project_Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY(`id),
);

  `name` VARCHAR(45) NOT NULL,
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
  PRIMARY KEY (`ID` )
);

CREATE TABLE `test_dashboard_schema`.`testSuite`
(
  `Test_Name` VARCHAR(45), --Refers to test in test suite
  `TestSuite` VARCHAR(45), --Refers to run of test
  -- `Time` FLOAT,
);

CREATE TABLE `test_dashboard_schema`.`test_names`
{
  `ID` INT,
  `test_name` varchar(45),
  `project` varchar(45);
  PRIMARY KEY (`ID`)
}

CREATE TABLE `test_dashboard_schema`.`testcase`
(
  `ID`  INT, --Needs to be unique because just about everything else repeats
  `Test ID` INT foreign key references (`test_dashboard_schema`.`test_names`),
  `TestSuite` VARCHAR(45) NOT NULL,
  `classname` VARCHAR(45) NOT NULL,
  `Time` FLOAT,
  `status` VARCHAR(45),
  `Launched` datetime(),
  PRIMARY KEY (`ID`)
);

CREATE TABLE `test_dashboard_schema`.`errors_and_failures`
(
    `test` INT foreign key references (`test_dashboard_schema`.`testcase`),
    `output` TEXT,
    `error/fail` boolean, --whether the test was an error or a fail
)
