import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule} from '@angular/forms'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProjectPageComponent } from './project-page/project-page.component';
import { TestListComponent } from './test-list/test-list.component';
import { OverviewComponent } from './overview/overview.component';
import { TestableComponent } from './testable/testable.component';
import { FailuresComponent } from './failures/failures.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
    AppComponent,
    ProjectPageComponent,
    TestListComponent,
    OverviewComponent,
    TestableComponent,
    FailuresComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
