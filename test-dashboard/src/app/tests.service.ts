import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TestsService {

  //baseUrl:string = "http://127.0.0.1/5000/"

  constructor(private http: HttpClient) { }

  getTestManifest(){
    return this.http.get('https://0.0.0.0/tests')
  }
//http://127.0.0.1:5000/api?action=test_overview&Project_id=1
  getTest(testId): any {
    //return this.http.get('https://0.0.0.0/testId')
    return this.http.get('http://127.0.0.1:5000/index')
  }

  getOverallSuccess(){
  //
   //return this.http.get<any>('http://127.0.0.1:5000/api?action=test_overview&Project_id=1')
   //console.log(this.http.get('https://127.0.0.1:5000/api?action=test_overview&Project_id=1').data);

   return this.http.get('https://127.0.0.1:5000/api?action=test_overview&Project_id=1')


  }
  getOverallFailure(){
    return this.http.get<any>('https://0.0.0.0/failure')

  }
  getOverallDNR(){
    return this.http.get<any>('https://0.0.0.0/DNR')

  }
  getRuntime(){
    return this.http.get<any>('https://0.0.0.0/runtime')

  }
}
