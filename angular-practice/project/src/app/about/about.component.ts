import { Component } from '@angular/core';
import { HomepageComponent } from '../homepage/homepage.component';
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-about',
  standalone: true,
  imports: [HomepageComponent, RouterLink, RouterOutlet],
  templateUrl: './about.component.html',
  styleUrl: './about.component.scss'
})
export class AboutComponent {

}
