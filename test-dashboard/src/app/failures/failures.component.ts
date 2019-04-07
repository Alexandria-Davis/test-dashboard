import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';


@Component({
  selector: 'app-failures',
  templateUrl: './failures.component.html',
  styleUrls: ['./failures.component.scss']
})
export class FailuresComponent implements OnInit {
  @Input() fail;
  @Output() onyell = new EventEmitter();

  testFail;
  results;

  // fireYellEvent(x){
  //   this.onyell.emit(x)
  // }
  constructor() { }

  ngOnInit() {
    this.testFail = 'Test Results';

    this.results = [
      {
        testName:"applicationForce",
       result:"Passed",
       time:"2:09",
       failures:"32"
    },
    {
      testName:"smokeTest1",
     result:"Passed",
     time:"10:09",
     failures:"1"
    },
    {
      testName:"hazeTest1",
     result:"Failed",
     time:"29:34",
     failures:"0"
    }
  ]
  }

}
