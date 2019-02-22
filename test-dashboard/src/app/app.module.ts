import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProjectPageComponent } from './project-page/project-page.component';
import { TestListComponent } from './test-list/test-list.component';
import { OverviewComponent } from './overview/overview.component';

@NgModule({
  declarations: [
    AppComponent,
    ProjectPageComponent,
    TestListComponent,
    OverviewComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
