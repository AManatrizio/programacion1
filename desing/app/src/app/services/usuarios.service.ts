import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class UsuariosService {
  url = '/api';
  constructor(private httpClient: HttpClient) {}

  getUsers(page: number = 1, perPage: number = 5) {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.get(
      `${this.url}/usuarios?page=${page}&per_page=${perPage}`,
      requestOptions
    );
  }

  getProfile() {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.get(`${this.url}/profile`, requestOptions);
  }
}