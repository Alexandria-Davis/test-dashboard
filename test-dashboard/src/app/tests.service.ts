import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TestsService {

  constructor(private http: HttpClient) { }

  getTestManifest(){
    return this.http.get('https://0.0.0.0/tests')
  }

  getTest(testId): any {
    return this.http.get('https://0.0.0.0/testId')
  }
  
  getOverallSuccess(){
    return this.http.get<any>('https://0.0.0.0/success')

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
