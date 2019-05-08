import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { test, testlist } from './test';
import {Observable, of } from 'rxjs'
@Injectable({
  providedIn: 'root'
})
export class TestsService {
  target_host = "http://localhost:5000";

  constructor(private http: HttpClient) { }

  getTestManifest(projName): Observable<testlist> {
    var response =  this.http.get<testlist>(`${this.target_host}/api?action=query_tests&Project_id=1`);
    console.log(response);
    return response;
    // let response = JSON.parse('{ "results": [ { "Last run": "Thu, 07 Mar 2019 00:00:00 GMT", "Project_id": 1, "Run_count": 20, "status": "passed", "test_name": "sample_passing_test" }, { "Last run": "Thu, 07 Mar 2019 00:00:00 GMT", "Project_id": 1, "Run_count": 20, "status": "failure", "test_name": "sample_failing_test" },{ "Last run": "Thu, 07 Mar 2019 00:00:00 GMT", "Project_id": 1, "Run_count": 20, "status": "passed", "test_name": "smoke_test_ums" }, { "Last run": "Thu, 07 Mar 2019 00:00:00 GMT", "Project_id": 1, "Run_count": 20, "status": "passed", "test_name": "sample_disabled_test" } ]}');
    // let test_arr = Array<test>();
    // for (let tests of response['results']){
    //   let testlist = new test;
    //   testlist.name = tests['test_name'];
    //   testlist.run_count = tests['Run_count'];
    //   testlist.status = tests['status'];
    //   testlist.last_run = tests["Last run"];
    //   testlist.project_id = tests['Project_id'];
    //   test_arr.push(testlist);
    // }
    // console.log(test_arr);
    // return of(test_arr);
  }

  getTest(testId): any {
    return this.http.get(`${this.target_host}/testId`)
  }

  getOverallSuccess(){
    return this.http.get<any>(`${this.target_host}/success`)

  }
  getOverallFailure(){
    return this.http.get<any>(`${this.target_host}/failure`)

  }
  getOverallDNR(){
    return this.http.get<any>(`${this.target_host}/DNR`)

  }
  getRuntime(){
    return this.http.get<any>(`${this.target_host}/runtime`)

  }
}
