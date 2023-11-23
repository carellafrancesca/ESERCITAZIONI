import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AreariservataService } from '../service/areariservata.service';
import { LoginRequest } from './LoginRequest';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {

  constructor(private router: Router, private areaRiservataSVC: AreariservataService){}

  navigateToHome(){
    this.router.navigate(['/homepage']);
  }

}
