import { Component } from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrl: './menu.component.css',
})
export class MenuComponent {
  get isToken() {
    return localStorage.getItem('token');
  }

  get admin_and_bibliotecary() {
    return (
      localStorage.getItem('rol') === 'admin' ||
      localStorage.getItem('rol') === 'bibliotecario'
    );
  }

  get is_admin() {
    return localStorage.getItem('rol') === 'admin';
  }

  get is_user() {
    return localStorage.getItem('rol') === 'user';
  }
}
