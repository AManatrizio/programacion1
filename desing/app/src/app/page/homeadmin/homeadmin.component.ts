import { Component } from '@angular/core';

@Component({
  selector: 'app-homeadmin',
  templateUrl: './homeadmin.component.html',
  styleUrl: './homeadmin.component.css',
})
export class HomeadminComponent {
  get admin_and_bibliotecary() {
    return (
      localStorage.getItem('rol') === 'admin' ||
      localStorage.getItem('rol') === 'bibliotecario'
    );
  }

  get is_admin() {
    return localStorage.getItem('rol') === 'admin';
  }
}
