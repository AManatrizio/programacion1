import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

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

    return this.httpClient.get(`${this.url}/usuarios/me`, requestOptions);
  }
  deleteUsers(id: number): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.delete(`${this.url}/usuario/${id}`, requestOptions);
  }

  getUserById(id: number): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };
    return this.httpClient.get(`${this.url}/usuario/${id}`, requestOptions);
  }

  updateUser(id: number, loanData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.put(
      `${this.url}/usuario/${id}`,
      loanData,
      requestOptions
    );
  }
}
