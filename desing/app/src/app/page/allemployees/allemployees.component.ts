import { Component } from '@angular/core';

@Component({
  selector: 'app-allemployees',
  templateUrl: './allemployees.component.html',
  styleUrl: './allemployees.component.css'
})
export class AllemployeesComponent {
  // Lista de empleados simulada (en tu caso, puede venir de un servicio o base de datos)
  employees = [
    { id: 1, name: 'Juan' },
    { id: 2, name: 'Maria' },
    { id: 3, name: 'Roberto' },
    { id: 4, name: 'Sofia' },
    { id: 5, name: 'Mario' }
  ];

  // Variable para almacenar el ID de búsqueda
  searchID: string = '';

  // Variable para almacenar los empleados filtrados
  filteredEmployees = [...this.employees];

  // Función de búsqueda
  searchEmployee() {
    const id = parseInt(this.searchID);
    
    if (!isNaN(id)) {
      // Filtra la lista de empleados por el ID
      this.filteredEmployees = this.employees.filter(employee => employee.id === id);
    } else {
      // Si no hay un ID válido, muestra todos los empleados
      this.filteredEmployees = [...this.employees];
    }
}
}
