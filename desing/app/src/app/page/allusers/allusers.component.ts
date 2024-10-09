import { Component } from '@angular/core';

@Component({
  selector: 'app-allusers',
  templateUrl: './allusers.component.html',
  styleUrl: './allusers.component.css',
})
export class AllusersComponent {
  // Lista de empleados simulada (en tu caso, puede venir de un servicio o base de datos)
  users = [
    { DNI: 45531057, name: 'Sofia' },
    { DNI: 45531054, name: 'Maria' },
    { DNI: 67899333, name: 'Roberto' },
    { DNI: 33333335, name: 'Gabriela' },
    { DNI: 23856248, name: 'Mario' },
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
      this.filteredUsers = this.users.filter((user) => user.DNI === id);
    } else {
      // Si no hay un ID válido, muestra todos los empleados
      this.filteredUsers = [...this.users];
    }
  }
}

// import { Component } from '@angular/core';
// import { Router } from '@angular/router';
// import { UsuariosService } from '../../../app/services/usuarios.service';

// @Component({
//   selector: 'app-allusers',
//   templateUrl: './allusers.component.html',
//   styleUrl: './allusers.component.css',
// })
// export class AllusersComponent {
//   // Lista de empleados simulada (en tu caso, puede venir de un servicio o base de datos)
//   users = [
//     { DNI: 45531057, name: 'Sofia' },
//     { DNI: 45531054, name: 'Maria' },
//     { DNI: 67899333, name: 'Roberto' },
//     { DNI: 33333335, name: 'Gabriela' },
//     { DNI: 23856248, name: 'Mario' },
//   ];

//   // Variable para almacenar el ID de búsqueda
//   searchID: string = '';

//   // Variable para almacenar los empleados filtrados
//   filteredUsers = [...this.users];
//   arrayUsuarios: any[] = [];
//   searchQuery = '';

//   constructor(
//     private router: Router,
//     private usuariosService: UsuariosService
//   ) {}

//   // Función de búsqueda

//   searchUsers() {
//     const id = parseInt(this.searchID);

//     if (!isNaN(id)) {
//       // Filtra la lista de empleados por el ID
//       this.filteredUsers = this.users.filter((user) => user.DNI === id);
//     } else {
//       // Si no hay un ID válido, muestra todos los empleados
//       this.filteredUsers = [...this.users];
//     }
//   }

//   buscar() {
//     console.log('buscar: ', this.searchQuery);
//     this.filteredUsers = this.arrayUsuarios.filter((user) =>
//       user.name.includes(this.searchQuery)
//     );
//   }

//   ngOnInit() {
//     this.usuariosService.getUsers().subscribe((rta: any) => {
//       console.log('usuarios api: ', rta);
//       this.arrayUsuarios = rta.usuarios || [];
//       this.filteredUsers = [...this.arrayUsuarios];
//     });
//   }

//   editarusuario(user: any) {
//     console.log('Estoy editando', user);
//     this.router.navigate(['/usuario/' + user.id + '/Editar']);
//   }
// }
