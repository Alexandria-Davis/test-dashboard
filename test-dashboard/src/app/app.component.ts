import { Component } from '@angular/core';
import { FailuresComponent } from './failures/index';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  //directives: [ FailuresComponent ]
})
export class AppComponent {
  title = 'Test-Dashboard';
  name = "fail";
  fail = {
    test1: "this is test 1",
    test2: "this is test 2"
  };

  yell(x){
    alert("testing");
  }
}
