import { Component, OnInit, Inject } from '@angular/core';
/*import { FailuresComponent } from './failures/index';*/
import {TestsService} from '../tests.service';
import { Observable } from 'rxjs';


@Component({
  selector: 'project-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.scss'],
  /*directives: [FailuresComponent]*/
})
export class OverviewComponent implements OnInit {
  results = [{
    "Last run": "Thu, 07 Mar 2019 00:00:00 GMT",
    "Project_id": 1,
    "Run_count": 23,
    "status": "passed",
    "test_name": "sample_passing_test"
  },
  {
    "Last run": "Thu, 07 Mar 2019 00:00:00 GMT",
    "Project_id": 1,
    "Run_count": 23,
    "status": "failure",
    "test_name": "sample_failing_test"
  },
  {
    "Last run": "Thu, 07 Mar 2019 00:00:00 GMT",
    "Project_id": 1,
    "Run_count": 23,
    "status": "passed",
    "test_name": "smoke_test_ums"
  },
  {
    "Last run": "Thu, 07 Mar 2019 00:00:00 GMT",
    "Project_id": 1,
    "Run_count": 23,
    "status": "passed",
    "test_name": "sample_disabled_test"
  }]

  passed;
  failed;
  durration;
  total;
  new_fail;
  no_run;
  title;

  constructor(private testService: TestsService) {
  }

  ngOnInit() {
    // /*Start Temp Data*/
    // this.passed = 3;
    // this.failed = 6;
    // this.no_run = 2;
    // this.total = this.passed + this.failed + this.no_run;
    // this.new_fail = 4;
    // this.durration = "34H 23M 11S";
    // /*End Temp Data*/
    // this.testService.getOverallSuccess().subscribe(
    //   data => {
    //     this.passed = data;
    //   }
    // );



    this.passed = this.testService.getOverallSuccess();
    this.failed = this.testService.getOverallFailure();
    this.no_run = this.testService.getOverallDNR();
    this.total = this.passed + this.failed + this.no_run;
    this.new_fail = 4;
    this.durration = this.testService.getRuntime();
    this.title = "Test Dashboard";
    console.log("hello");
    console.log(this.passed);
  }


}
