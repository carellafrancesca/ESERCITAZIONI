import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { AboutComponent } from '../about/about.component';
import { HomepageComponent } from '../homepage/homepage.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-feedback',
  standalone: true,
  imports: [RouterLink, RouterOutlet, AboutComponent, HomepageComponent, CommonModule, FormsModule],
  templateUrl: './feedback.component.html',
  styleUrl: './feedback.component.scss'
})
export class FeedbackComponent {

  feedback = {
    name: '',
    email: '',
    message: '',
  }

  showConfirmationMessage: boolean = false;
  showErrorMessage: boolean = false;

  submitForm(){
    const isFeedbackSentSuccessfully = true;

    if(isFeedbackSentSuccessfully){
      this.showConfirmationMessage = true;
      this.showErrorMessage = false;
      console.log("Messaggio inviato con successo!");
      this.resetForm();
    } else {
      this.showConfirmationMessage = false;
      this.showErrorMessage = true;
    }
  }

  resetForm(){
    this.feedback = {
      name: '',
      email: '',
      message: ''
    }
  }

}
