import { Component } from '@angular/core';

@Component({
  selector: 'app-allbooks',
  templateUrl: './allbooks.component.html',
  styleUrl: './allbooks.component.css'
})
export class AllbooksComponent {
  // Lista de empleados simulada (en tu caso, puede venir de un servicio o base de datos)
  books = [
    { id: 1, name: 'Harry Potter y la piedra filosofal' },
    { id: 2, name: 'Harry Potter  y la camara secreta' },
    { id: 3, name: 'RHarry Potter 3' },
    { id: 4, name: 'The Great Gatsby' },
    { id: 5, name: 'Juego de tronos' }
  ];

  // Variable para almacenar el ID de búsqueda
  searchID: string = '';

  // Variable para almacenar los empleados filtrados
  filteredEmployees = [...this.books];

  // Función de búsqueda
  searchEmployee() {
    const id = parseInt(this.searchID);
    
    if (!isNaN(id)) {
      // Filtra la lista de empleados por el ID
      this.filteredEmployees = this.books.filter(employee => employee.id === id);
    } else {
      // Si no hay un ID válido, muestra todos los empleados
      this.filteredEmployees = [...this.books];
    }
}
}