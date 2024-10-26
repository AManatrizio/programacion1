import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable, take } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class LoansService {
  url = '/api';
  constructor(private httpClient: HttpClient) {}

  getLoans(
    page: number = 1,
    perPage: number = 5,
    searchField: string = 'prestamo',
    searchQuery: string = ''
  ) {
    const auth_token = localStorage.getItem('token');

    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    let params = new HttpParams()
      .set('page', page.toString())
      .set('per_page', perPage.toString());

    if (searchField && searchQuery) {
      params = params.set(searchField, searchQuery);
    }

    const requestOptions = { headers: headers, params: params };

    return this.httpClient.get(`${this.url}/prestamos`, requestOptions);
  }

  addLoans(userData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.post(
      this.url + '/prestamos',
      userData,
      requestOptions
    );
  }

  deleteLoans(id: number): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.delete(`${this.url}/prestamo/${id}`, requestOptions);
  }

  getLoanById(id: number): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };
    return this.httpClient.get(`${this.url}/prestamo/${id}`, requestOptions);
  }

  updateLoan(id: number, loanData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.put(
      `${this.url}/prestamo/${id}`,
      loanData,
      requestOptions
    );
  }
}
