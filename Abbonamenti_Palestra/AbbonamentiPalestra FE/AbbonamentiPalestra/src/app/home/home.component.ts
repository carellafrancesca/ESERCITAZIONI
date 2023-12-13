import { Component, OnInit } from '@angular/core';
import { AttivitaService } from '../service/attivita.service';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { RouterOutlet, RouterLink } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [HttpClientModule, RouterOutlet, RouterLink, FormsModule, CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit{

  tipiAttivita: string[] = [];

  constructor(private tipiAttivitaService: AttivitaService) { }

  ngOnInit() {
    this.caricaTipiAttivita();
  }

  caricaTipiAttivita() {
    this.tipiAttivitaService.getTipiAttivita()
      .subscribe(response => {
        this.tipiAttivita = response;
      }, error => {
        console.log('Errore nel recupero dei dati');
      });
  }

}
