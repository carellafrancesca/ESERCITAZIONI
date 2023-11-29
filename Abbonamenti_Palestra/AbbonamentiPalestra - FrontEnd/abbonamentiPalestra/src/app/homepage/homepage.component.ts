import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Route, Router } from '@angular/router';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrl: './homepage.component.scss'
})
export class HomepageComponent {

  constructor(private router: Router){}

  navigateToActivity(){
    this.router.navigate(['/activity']);
  }

}
