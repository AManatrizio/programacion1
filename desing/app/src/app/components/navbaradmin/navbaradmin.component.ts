import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-navbaradmin',
  templateUrl: './navbaradmin.component.html',
  styleUrl: './navbaradmin.component.css',
})
export class NavbaradminComponent {
  ver = true;

  constructor(private authService: AuthService) {}

  get isToken() {
    return localStorage.getItem('token');
  }

  cerrarSesion() {
    this.authService.logout();
  }
}
