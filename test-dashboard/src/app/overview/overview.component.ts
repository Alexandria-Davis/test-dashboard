import { Component, OnInit, Inject } from '@angular/core';
/*import { FailuresComponent } from './failures/index';*/
import {TestsService} from '../tests.service';
import { Observable, of } from 'rxjs';
import {test, testlist } from '../test';
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'project-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.scss'],
  /*directives: [FailuresComponent]*/
})
export class OverviewComponent implements OnInit {
  passed: number = 0;
  failed: number = 0;
  durration: number = 0;
  total: number = 0;
  new_fail;
  no_run: number = 0;
  title;
  tests : test[];
  // tests : test[] = [
  //   {last_run: "Thu, 07 Mar 2019 00:00:00 GMT", name: "sample_passing_test", status: "passed", test_id: "5", test_name_id: "1", time: 7.38},
  //   {last_run: "Thu, 07 Mar 2019 00:00:00 GMT", name: "sample_failing_test", status: "failure", test_id: "5", test_name_id: "1", time: 7.38},
  //   {last_run: "Thu, 07 Mar 2019 00:00:00 GMT", name: "sample_ignore_test", status: "ignored", test_id: "5", test_name_id: "1", time: 7.38},
  //   {last_run: "Thu, 07 Mar 2019 00:00:00 GMT", name: "sample_passing_test2", status: "passed", test_id: "5", test_name_id: "1", time: 7.38}
  //   ];
  project_name: string;

  constructor(private testService: TestsService, private route: ActivatedRoute) {
  }

  ngOnInit() {
    this.getTestManifest();  //uncomment on live

  }
  deal_with_stuff(results:testlist): void{
    console.log(results)
    this.project_name = results.Project;
    this.tests = results.results;
    for(let test of this.tests){
      if(test.status == "passed"){
        this.passed += 1;
      }
      else if( test.status == "ignored"){
        this.no_run += 1;
      }
      else{
        this.failed +=1;
      }
      this.durration += Math.floor(test.time);
    }
    this.total = this.passed + this.failed + this.no_run;
  }
  getTestManifest(): void{
    this.route.params.subscribe(
      params => this.testService.getTestManifest(params['id'])
        .subscribe(tests => this.deal_with_stuff(tests))
    );
  }

}
