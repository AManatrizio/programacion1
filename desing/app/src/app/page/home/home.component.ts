import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
})
export class HomeComponent {
  get admin_and_bibliotecary() {
    return (
      localStorage.getItem('rol') === 'admin' ||
      localStorage.getItem('rol') === 'bibliotecary'
    );
  }
}
