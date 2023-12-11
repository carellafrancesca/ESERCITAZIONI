import { Routes } from '@angular/router';
import { HomepageComponent } from './homepage/homepage.component';
import { AboutComponent } from './about/about.component';
import { FeedbackComponent } from './feedback/feedback.component';

export const routes: Routes = [
  { path: '', component: HomepageComponent},
  { path: 'homepage', component: HomepageComponent},
  { path: 'about', component: AboutComponent},
  { path: 'feedback', component: FeedbackComponent},
];
