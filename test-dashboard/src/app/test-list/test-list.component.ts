import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'project-test-list',
  templateUrl: './test-list.component.html',
  styleUrls: ['./test-list.component.scss']
})
export class TestListComponent implements OnInit {
  tests;
  constructor() { }

  ngOnInit() {
    this.tests = [
      {
        test_name:"sample_test_1",
        durration:"3M",
        status:"Pass",
        historical_pass_rate:"50%",
        historical_run_rate:"100%"
      },
      {
        test_name:"sample_test_2",
        durration:"2H1M3s",
        status:"Fail",
        historical_pass_rate:"0%",
        historical_run_rate:"40%"
      },
      {
        test_name:"sample_test_3",
        durration:"0H0M0S",
        status:"Did Not Run",
        historical_pass_rate:"0%",
        historical_run_rate:"0%"
      },
    ]
  }
}
