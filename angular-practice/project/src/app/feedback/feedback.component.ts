import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { AboutComponent } from '../about/about.component';
import { HomepageComponent } from '../homepage/homepage.component';

@Component({
  selector: 'app-feedback',
  standalone: true,
  imports: [RouterLink, RouterOutlet, AboutComponent, HomepageComponent],
  templateUrl: './feedback.component.html',
  styleUrl: './feedback.component.scss'
})
export class FeedbackComponent {

}
