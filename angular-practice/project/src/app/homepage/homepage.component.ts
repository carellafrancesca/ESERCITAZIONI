import { Component, NgModule } from '@angular/core';
import { AboutComponent } from '../about/about.component';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { FormsModule, NgModel } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { FeedbackComponent } from '../feedback/feedback.component';

@Component({
  selector: 'app-homepage',
  standalone: true,
  imports: [AboutComponent, RouterLink, RouterOutlet, FormsModule, CommonModule, FeedbackComponent],
  templateUrl: './homepage.component.html',
  styleUrl: './homepage.component.scss'
})
export class HomepageComponent {

  username: string = '';
  cityFilter: string = '';
  cities: string[] = [];
  randomCity: string = '';
  timer: number = 0;
  timerRunning: boolean = false;

  constructor(){
    this.cities = ['Roma', 'Milano', 'Torino', 'Padova', 'Bari', 'Bologna', 'Firenze', 'Napoli'];
  }

  submitForm(){
    console.log('Submitted! Username:', this.username);
  }

  submitFormCity(){
    console.log('Search button clicked! City Filter:', this.cityFilter);
  }

  getRandomCity(): string{
    const randomIndex = Math.floor(Math.random() * this.cities.length);
    return this.cities[randomIndex];
  }

  /*
  Math.random(): Restituisce un numero casuale in virgola mobile compreso tra 0 (incluso) e 1 (escluso).
  this.cities.length: Restituisce la lunghezza dell'array this.cities, cioè il numero totale di città presenti nell'array.
  Math.floor(): Arrotonda un numero verso il basso all'intero più vicino. Questo è usato per ottenere un numero intero dalla parte intera del risultato di Math.random() * this.cities.length, garantendo che sia un numero intero compreso tra 0 e this.cities.length - 1.
  this.cities[randomIndex]: Accede all'elemento dell'array this.cities corrispondente all'indice generato casualmente (randomIndex), restituendo quindi una città casuale dall'array.
  */

  submitFormRandomCity(){
    this.randomCity = this.getRandomCity();
    console.log("Random city: ", this.randomCity);
  }

  startTimer(){
    this.timerRunning = true;
    this.updateTimer();
  }

  stopTimer(){
    this.timerRunning = false;
  }

  resetTimer(){
    this.timer = 0;
    this.stopTimer();
  }

  private updateTimer(){
    if(this.timerRunning){
      setTimeout(() => {
        this.timer++;
        this.updateTimer();
      }, 1000);
    }
  }

  /*updateTimer() è una funzione ricorsiva che utilizza setTimeout per incrementare il timer ogni secondo finché timerRunning è true. Quando timerRunning diventa false (fermando il timer), la funzione ricorsiva smette di chiamarsi, interrompendo il ciclo e mantenendo il valore del timer invariato.*/


}
