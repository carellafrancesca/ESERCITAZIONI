import { HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TipologieService } from '../service/tipologie.service';

@Component({
  selector: 'app-activity',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './activity.component.html',
  styleUrl: './activity.component.scss'
})
export class ActivityComponent implements OnInit{

  tipiAttivita!: string[];
  tipiAbbonamento!: string[];

  constructor(private tipoSvc: TipologieService) {}

  ngOnInit(): void {
    this.tipoSvc.getTipiAttivita().subscribe(data => {
      this.tipiAttivita = data;
    });

    this.tipoSvc.getTipiAbbonamento().subscribe(data => {
      this.tipiAbbonamento = data;
    });
  }



}
