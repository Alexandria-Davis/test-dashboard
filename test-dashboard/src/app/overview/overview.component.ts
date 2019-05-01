import { Component, OnInit, Inject } from '@angular/core';
/*import { FailuresComponent } from './failures/index';*/
import {TestsService} from '../tests.service';
import { Observable, of } from 'rxjs';
import {test, testlist } from '../test';

@Component({
  selector: 'project-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.scss'],
  /*directives: [FailuresComponent]*/
})
export class OverviewComponent implements OnInit {
  // results = [{
  //   "Last run": "Thu, 07 Mar 2019 00:00:00 GMT",
  //   "Project_id": 1,
  //   "Run_count": 23,
  //   "status": "passed",
  //   "test_name": "sample_passing_test"
  // },
  // {
  //   "Last run": "Thu, 07 Mar 2019 00:00:00 GMT",
  //   "Project_id": 1,
  //   "Run_count": 23,
  //   "status": "failure",
  //   "test_name": "sample_failing_test"
  // },
  // {
  //   "Last run": "Thu, 07 Mar 2019 00:00:00 GMT",
  //   "Project_id": 1,
  //   "Run_count": 23,
  //   "status": "passed",
  //   "test_name": "smoke_test_ums"
  // },
  // {
  //   "Last run": "Thu, 07 Mar 2019 00:00:00 GMT",
  //   "Project_id": 1,
  //   "Run_count": 23,
  //   "status": "passed",
  //   "test_name": "sample_disabled_test"
  // }]

  passed;
  failed;
  durration;
  total;
  new_fail;
  no_run;
  title;
  tests : test[];
  //goodTests : Object

  constructor(private testService: TestsService) {
  }

  ngOnInit() {
    this.getTestManifest();
  
    //console.log("After subscribe call  " , this.tests)
    // let evilResponseProps = Object.keys(test);
    // // Step 2. Create an empty array.
    // let goodTests = [];
    // // Step 3. Iterate throw all keys.
    // for (prop of evilResponseProps) {
    //   goodTests.push(evilResponseProps[prop]);
    // }
    // return goodTests;
    // console.log(this.tests)
    //this.tests = this.testService.getTestManifest(1);
    // /*Start Temp Data*/
    // this.passed = 3;
    // this.failed = 6;
    // this.no_run = 2;
    // this.total = this.passed + this.failed + this.no_run;
    // this.new_fail = 4;s
    // this.durration = "34H 23M 11S";
    // /*End Temp Data*/

  }
  deal_with_stuff(results:testlist): void{
    console.log(results)
    this.tests = results.results;
    //console.log(results,"!!!!!!!");
    console.log("tests is set", this.tests[2]);
  }
  getTestManifest(): void{
    this.testService.getTestManifest(1)
        .subscribe(tests => this.deal_with_stuff(tests));
  }

}
