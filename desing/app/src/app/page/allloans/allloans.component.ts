import { Component } from '@angular/core';

@Component({
  selector: 'app-allloans',
  templateUrl: './allloans.component.html',
  styleUrl: './allloans.component.css',
})
export class AllloansComponent {
  // Lista de empleados simulada (en tu caso, puede venir de un servicio o base de datos)
  loans = [
    { id: 1, book: 'El Hobbit', IDUser: 1 },
    { id: 2, book: 'Harry Potter 1', IDUser: 2 },
    { id: 3, book: '1984', IDUser: 3 },
    { id: 4, book: 'The Great Gatsby', IDUser: 4 },
    { id: 5, book: 'Harry Potter y la piedra filosofal', IDUser: 5 },
    { id: 6, book: 'Harry Potter  y la camara secreta', IDUser: 6 },
  ];

  // Variable para almacenar el ID de búsqueda
  searchID: string = '';

  // Variable para almacenar los empleados filtrados
  filteredLoan = [...this.loans];

  // Función de búsqueda
  searchLoan() {
    const id = parseInt(this.searchID);

    if (!isNaN(id)) {
      // Filtra la lista de empleados por el ID
      this.filteredLoan = this.loans.filter((loan) => loan.id === id);
    } else {
      // Si no hay un ID válido, muestra todos los empleados
      this.filteredLoan = [...this.loans];
    }
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
}
