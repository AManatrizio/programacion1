import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { catchError, map, Observable, take, throwError } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class OpinionsService {
  private url = '/api';

  constructor(private httpClient: HttpClient) {}

  addOpinion(prestamo_id: number, opinionData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    const body = {
      ...opinionData,
    };

    return this.httpClient.post(
      `${this.url}/opiniones/addopinion/${prestamo_id}`,
      body,
      requestOptions
    );
  }

  updateOpinion(prestamo_id: number, opinionData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    console.log('Actualizando opinión para préstamo ID:', prestamo_id);
    return this.httpClient.put(
      `${this.url}/opinion/editopinion/${prestamo_id}`,
      opinionData,
      requestOptions
    );
  }

  getOpinionesByUser(): Observable<any> {
    const auth_token = localStorage.getItem('token');

    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    return this.httpClient.get(`${this.url}/opiniones`, { headers });
  }

  getOpinionByLoanId(prestamo_id: number): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    console.log('Solicitando opinión para préstamo ID:', prestamo_id);
    return this.httpClient.get(
      `${this.url}/opinion/${prestamo_id}`,
      requestOptions
    );
  }

  getResenasByLibroId(libroId: number): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.get(
      `${this.url}/resenas/libro/${libroId}`,
      requestOptions
    );
  }
}
