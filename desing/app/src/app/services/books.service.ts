import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class BooksService {
  url = '/api';
  constructor(private httpClient: HttpClient) {}

  getBooks(page: number = 1, perPage: number = 5) {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.get(
      `${this.url}/libros?page=${page}&per_page=${perPage}`,
      requestOptions
    );
  }
}
