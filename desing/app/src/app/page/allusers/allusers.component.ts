import { Component } from '@angular/core';

@Component({
  selector: 'app-allusers',
  templateUrl: './allusers.component.html',
  styleUrl: './allusers.component.css'
})
export class AllusersComponent {
 // Lista de empleados simulada (en tu caso, puede venir de un servicio o base de datos)
 users = [
  { DNI: 45531057, name: 'Sofia' },
  { DNI: 45531054, name: 'Maria' },
  { DNI: 67899333, name: 'Roberto' },
  { DNI: 33333335, name: 'Gabriela' },
  { DNI: 23856248, name: 'Mario' }
];

// Variable para almacenar el ID de búsqueda
searchID: string = '';

// Variable para almacenar los empleados filtrados
filteredUsers = [...this.users];

// Función de búsqueda
searchUsers() {
  const id = parseInt(this.searchID);
  
  if (!isNaN(id)) {
    // Filtra la lista de empleados por el ID
    this.filteredUsers = this.users.filter(user => user.DNI === id);
  } else {
    // Si no hay un ID válido, muestra todos los empleados
    this.filteredUsers = [...this.users];
  }
}
}
