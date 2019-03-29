import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProjectPageComponent } from './project-page/project-page.component';
import { TestableComponent } from './testable/testable.component';

import { FailuresComponent } from './failures/failures.component';

const routes: Routes = [
  {
    path:'project/:id',
    component: ProjectPageComponent
  },
  {
    path:'project',
    component: ProjectPageComponent
  },
  {
    path:'',
    component: ProjectPageComponent
  },
  {
    path:'test', //area reserved for testing our stuff
    component: TestableComponent
  },
  {
    path:'failures',
    component: FailuresComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
