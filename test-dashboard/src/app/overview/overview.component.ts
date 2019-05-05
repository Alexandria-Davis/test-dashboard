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

  passed;
  failed;
  durration;
  total;
  new_fail;
  no_run;
  title;
  tests : test[];
  project_name: string;

  constructor(private testService: TestsService, private route: ActivatedRoute) {
  }

  ngOnInit() {
    this.getTestManifest();

  }
  deal_with_stuff(results:testlist): void{
    console.log(results)
    this.project_name = results.Project;
    this.tests = results.results;
    //console.log(results,"!!!!!!!");
    console.log("tests is set", this.tests[2]);
  }
  getTestManifest(): void{
    this.route.params.subscribe(
      params => this.testService.getTestManifest(params['id'])
        .subscribe(tests => this.deal_with_stuff(tests))
    );
  }

}
