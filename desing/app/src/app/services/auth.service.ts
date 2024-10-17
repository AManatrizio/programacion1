import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, take } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  url = '/api'; // Asegúrate de que esta URL esté correctamente configurada
  constructor(private httpClient: HttpClient, private router: Router) {}

  // Observable (Libreria Reactiva Angular) permite susbrirse a una fuente de datos que puede emitir multiples valores
  login(dataLogin: any): Observable<any> {
    return (
      this.httpClient
        //Definicion de ruta particular
        .post(this.url + '/auth/login', dataLogin)
        // Llamar al login por unica vez cuando se llame a login
        .pipe(take(1))
    );
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('rol');
    this.router.navigateByUrl('home');
  }
}
