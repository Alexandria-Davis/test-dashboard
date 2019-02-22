import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProjectPageComponent } from './project-page/project-page.component';


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
    path:'',
    component: ProjectPageComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
