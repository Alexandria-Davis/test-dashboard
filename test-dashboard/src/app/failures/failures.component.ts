import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-failures',
  templateUrl: './failures.component.html',
  styleUrls: ['./failures.component.scss']
})
export class FailuresComponent implements OnInit {
  @Input() fail;
  @Output() onyell = new EventEmitter();

  fireYellEvent(x){
    this.onyell.emit(x)
  }
  constructor() { }

  ngOnInit() {
  }

}
