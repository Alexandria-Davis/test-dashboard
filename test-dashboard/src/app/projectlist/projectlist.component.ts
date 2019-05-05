import { Component, OnInit } from '@angular/core';
import {Project, Project_Wrap} from '../project'
import {TestsService} from '../tests.service';
@Component({
  selector: 'app-projectlist',
  templateUrl: './projectlist.component.html',
  styleUrls: ['./projectlist.component.scss']
})
export class ProjectlistComponent implements OnInit {
  project_listings: Project[];
  constructor(private testService: TestsService) {  }

  ngOnInit() {
    this.testService.get_projects()
      .subscribe(projects => this.project_listings = projects.results);
  }

}
