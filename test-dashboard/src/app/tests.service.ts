import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { test, testlist } from './test';
import {Observable, of } from 'rxjs'
import {Project, Project_Wrap} from './project'
@Injectable({
  providedIn: 'root'
})
export class TestsService {
url_base = 'http://127.0.0.1:5000'
  constructor(private http: HttpClient) { }

  get_projects(): Observable<Project_Wrap> {
    var response = this.http.get<Project_Wrap>(`${this.url_base}/api?action=query_projects`);

    return response;
  }

  getTestManifest(projId): Observable<testlist> {
    var response =  this.http.get<testlist>(`${this.url_base}/api?action=query_tests&Project_id=${projId}`);
    return response;
  }
//http://127.0.0.1:5000/api?action=test_overview&Project_id=1
  getTest(testId): any {
    //return this.http.get('https://0.0.0.0/testId')
    return this.http.get('${this.url_base}/api?action=')
  }
}
