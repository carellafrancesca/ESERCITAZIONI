import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AttivitaService {

  private attivitaUrl = 'http://localhost:8080/api/tipi/attivita';

  constructor(private http: HttpClient) { }

  /*getTipiAttivita(): Observable<string[]>{
    return this.http.get<string[]>(this.attivitaUrl);
  }*/

}
