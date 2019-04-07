import { Component, OnInit } from '@angular/core';
/*import { FailuresComponent } from './failures/index';*/
import {TestsService} from '../tests.service';

@Component({
  selector: 'project-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.scss'],
  /*directives: [FailuresComponent]*/
})
export class OverviewComponent implements OnInit {
  passed;
  failed;
  durration;
  total;
  new_fail;
  no_run;

  constructor(private testService: TestsService) { }

  ngOnInit() {
    // /*Start Temp Data*/
    // this.passed = 3;
    // this.failed = 6;
    // this.no_run = 2;
    // this.total = this.passed + this.failed + this.no_run;
    // this.new_fail = 4;
    // this.durration = "34H 23M 11S";
    // /*End Temp Data*/
    this.passed = this.testService.getOverallSuccess();
    this.failed = this.testService.getOverallFailure();
    this.no_run = this.testService.getOverallDNR();
    this.total = this.passed + this.failed + this.no_run;
    this.new_fail = 4;
    this.durration = this.testService.getRuntime();
  }


}
