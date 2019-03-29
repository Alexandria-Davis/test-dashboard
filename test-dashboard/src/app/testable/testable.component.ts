import { Component, OnInit } from '@angular/core';
import { ReadXmlService} from '../read-xml.service'

@Component({
  selector: 'app-testable',
  templateUrl: './testable.component.html',
  styleUrls: ['./testable.component.scss']
})
export class TestableComponent implements OnInit {

  TestOut;
  FromXML;

  constructor(public readXML: ReadXmlService) { }

  ngOnInit() {
    this.TestOut = "this is a text";
    this.readXML.set_dummies();
    this.FromXML = this.readXML.read_xml_data();
  }

}
