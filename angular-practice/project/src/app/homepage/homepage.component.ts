import { Component } from '@angular/core';
import { AboutComponent } from '../about/about.component';
import { Router, RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-homepage',
  standalone: true,
  imports: [AboutComponent, RouterLink, RouterOutlet],
  templateUrl: './homepage.component.html',
  styleUrl: './homepage.component.scss'
})
export class HomepageComponent {

}
