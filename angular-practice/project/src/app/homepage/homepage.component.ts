import { Component, NgModule } from '@angular/core';
import { AboutComponent } from '../about/about.component';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { FormsModule, NgModel } from '@angular/forms';

@Component({
  selector: 'app-homepage',
  standalone: true,
  imports: [AboutComponent, RouterLink, RouterOutlet, FormsModule],
  templateUrl: './homepage.component.html',
  styleUrl: './homepage.component.scss'
})
export class HomepageComponent {

  username: string = '';

  submitForm(){
    console.log('Submitted! Username:', this.username);
  }

}
