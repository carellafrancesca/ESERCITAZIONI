import { Routes } from '@angular/router';
import { HomepageComponent } from './homepage/homepage.component';
import { ActivityComponent } from './activity/activity.component';

export const routes: Routes = [
  { path: '', component: HomepageComponent },
  { path: 'homepage', component: HomepageComponent },
  { path: 'activity', component: ActivityComponent },
];
