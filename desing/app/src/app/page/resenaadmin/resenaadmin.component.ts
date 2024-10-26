import { Component } from '@angular/core';

@Component({
  selector: 'app-resenaadmin',
  templateUrl: './resenaadmin.component.html',
  styleUrl: './resenaadmin.component.css',
})
export class ResenaadminComponent {
  get admin_and_librarian() {
    return (
      localStorage.getItem('rol') === 'admin' ||
      localStorage.getItem('rol') === 'librarian'
    );
  }
}
