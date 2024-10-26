import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, take } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class BooksService {
  url = '/api';
  constructor(private httpClient: HttpClient) {}

  getBooks(page: number = 1, perPage: number = 5, searchQuery: string = '') {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    const searchParam = searchQuery ? `&genero=${searchQuery}` : '';

    return this.httpClient.get(
      `${this.url}/libros?page=${page}&per_page=${perPage}${searchParam}`,
      requestOptions
    );
  }

  addBooks(userData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
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
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.delete(`${this.url}/libro/${id}`, requestOptions);
  }

  getBooksById(id: number): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };
    return this.httpClient.get(`${this.url}/libro/${id}`, requestOptions);
  }

  updateBooks(id: number, loanData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.put(
      `${this.url}/libro/${id}`,
      loanData,
      requestOptions
    );
  }
}
