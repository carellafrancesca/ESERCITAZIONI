import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TipologieService {

  private apiUrl = 'http://localhost:8080/api/tipi';

  constructor(private http: HttpClient) {}

  getTipiAttivita(): Observable<string[]> {
    return this.http.get<string[]>(`${this.apiUrl}/attivita`);
  }

  getTipiAbbonamento(): Observable<string[]> {
    return this.http.get<string[]>(`${this.apiUrl}/abbonamento`);
  }

}
