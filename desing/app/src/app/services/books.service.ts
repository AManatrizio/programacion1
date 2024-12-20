import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable, take } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class BooksService {
  url = '/api';
  constructor(private httpClient: HttpClient) {}

  getBooks(
    page: number = 1,
    perPage: number = 4,
    searchField: string = 'nombre',
    searchQuery: string = ''
  ) {
    const auth_token = localStorage.getItem('token');

    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    let params = new HttpParams()
      .set('page', page.toString())
      .set('per_page', perPage.toString());

    if (searchField && searchQuery) {
      params = params.set(searchField, searchQuery);
    }

    const requestOptions = { headers: headers, params: params };

    return this.httpClient.get(`${this.url}/libros`, requestOptions);
  }

  addBooks(userData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.post(
      this.url + '/libros/addbooks',
      userData,
      requestOptions
    );
  }

  deleteBooks(id: number): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.delete(`${this.url}/libro/${id}`, requestOptions);
  }

  getBooksById(id: number): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };
    return this.httpClient.get(`${this.url}/libro/${id}`, requestOptions);
  }

  updateBooks(id: number, loanData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.put(
      `${this.url}/libro/${id}`,
      loanData,
      requestOptions
    );
  }

  getLibrosMejorValorados(): Observable<any[]> {
    return this.httpClient.get<any[]>(`${this.url}/libros/mejorvalorados`);
  }
}
