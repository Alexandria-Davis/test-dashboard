CREATE SCHEMA `test_dashboard_schema` ;

CREATE TABLE `test_dashboard_schema`.`projects`
(
  `id` int NOT NULL,
  `Project_Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY(`id`),
);


  `name` VARCHAR(45) NOT NULL,
CREATE TABLE `test_dashboard_schema`.`testrun` ( --top level of xml file
  `ID` INT,
  `Name` VARCHAR(45) NOT NULL,
  `Project` int(45) foreign key references(`test_dashboard_schema`.`projects`), --Refers to project that the tests belongs to
  --`test count` VARCHAR(45) NULL, --can calculate
  --`Started` VARCHAR(45) NULL, --can calculate
  --`Failed` VARCHAR(45) NULL, --can calculate
  --`Errors` VARCHAR(45) NULL, --can calculate
  --`Ignores` VARCHAR(45) NULL, --can calculate
  `date` datetime(),
  PRIMARY KEY (`ID` )
);

CREATE TABLE `test_dashboard_schema`.`testSuite`
(
  `TestSuite` VARCHAR(45), --Refers to run of test
  `Project` INT fOREIGN KEY REFERENCES (`test_dashboard_schema`.`projects`)
  `RunTime` FLOAT,
);

CREATE TABLE `test_dashboard_schema`.`test_names`
{
  `ID` INT,
  `test_name` varchar(45),
  `project` INT fOREIGN KEY REFERENCES (`test_dashboard_schema`.`projects`);
  PRIMARY KEY (`ID`)
}

CREATE TABLE `test_dashboard_schema`.`testcase`
(
  `ID`  INT, --Needs to be unique because just about everything else repeats
  `Test ID` INT foreign key references (`test_dashboard_schema`.`test_names`),
  `TestSuite` VARCHAR(45) NOT NULL,
  `classname` VARCHAR(45) NOT NULL,
  `Time` FLOAT,
  `status` VARCHAR(10),
  `Launched` datetime(),
  PRIMARY KEY (`ID`)
);

CREATE TABLE `test_dashboard_schema`.`errors_and_failures`
(
    `test` INT foreign key references (`test_dashboard_schema`.`testcase`),
    `output` TEXT,
    `status` VARCHAR(10), --whether the test was an error or a fail
)
