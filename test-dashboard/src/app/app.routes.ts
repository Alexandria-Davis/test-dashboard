import { FailuresComponent } from "./failures/failures.component";
import { OverviewComponent } from "./overview/overview.component";
import { provideRoutes } from "@angular/router";


const APP_ROUTES = [
  { path: 'failures', component: FailuresComponent },
  { path: '', component: OverviewComponent }
];

export const APP_ROUTES_PROVIDED = [
  provideRoutes(APP_ROUTES)
];
