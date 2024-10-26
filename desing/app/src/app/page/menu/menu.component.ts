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

  get admin_and_librarian() {
    return (
      localStorage.getItem('rol') === 'admin' ||
      localStorage.getItem('rol') === 'librarian'
    );
  }

  get is_admin() {
    return localStorage.getItem('rol') === 'admin';
  }

  get is_user() {
    return localStorage.getItem('rol') === 'user';
  }
}
