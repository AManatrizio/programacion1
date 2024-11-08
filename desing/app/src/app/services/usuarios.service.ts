import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class UsuariosService {
  url = '/api';
  constructor(private httpClient: HttpClient) {}

  getUsers(
    page: number = 1,
    perPage: number = 5,
    searchField: string = 'prestamo',
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

    return this.httpClient.get(`${this.url}/usuarios`, requestOptions);
  }

  getProfile() {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.get(`${this.url}/usuarios/me`, requestOptions);
  }
  deleteUsers(id: number): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.delete(`${this.url}/usuario/${id}`, requestOptions);
  }

  getUserById(id: number): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };
    return this.httpClient.get(`${this.url}/usuario/${id}`, requestOptions);
  }

  updateUser(id: number, loanData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Authorization: `Bearer ${auth_token}`,
    });

    const requestOptions = { headers: headers };

    return this.httpClient.put(
      `${this.url}/usuario/${id}`,
      loanData,
      requestOptions
    );
  }
}
