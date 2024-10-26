import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UsuariosService } from '../../services/usuarios.service';

@Component({
  selector: 'app-allemployees',
  templateUrl: './allemployees.component.html',
  styleUrl: './allemployees.component.css',
})
export class AllemployeesComponent {
  arrayUsuarios: any[] = [];
  filteredUsers: any[] = [];

  searchQuery: string = '';
  searchField: string = 'nombre';
  currentPage: number = 1;
  perPage: number = 5;
  totalPages: number = 1;
  constructor(
    private router: Router,
    private empleadosService: UsuariosService
  ) {}

  ngOnInit() {
    this.loadUsers();
  }

  loadUsers() {
    this.empleadosService
      .getUsers(
        this.currentPage,
        this.perPage,
        this.searchField,
        this.searchQuery
      )
      .subscribe(
        (rta: any) => {
          console.log('Respuesta del API:', rta);
          this.arrayUsuarios = rta.usuarios.filter(
            (usuarios: any) => usuarios.rol === 'librarian'
          );
          this.filteredUsers = [...this.arrayUsuarios];
          this.totalPages = rta.pages;
        },
        (error) => {
          console.error('Error al obtener prestamos:', error);
        }
      );
  }

  editarusuario(user: any) {
    console.log('Estoy editando', user);
    this.router.navigate(['/usuario/' + user.id + '/Editar']);
  }

  buscar() {
    const searchQueryLowerCase = this.searchQuery.trim().toLowerCase();
    console.log('buscar: ', searchQueryLowerCase);
    this.filteredUsers = this.arrayUsuarios.filter((user) =>
      user.nombre.toLowerCase().includes(searchQueryLowerCase)
    );
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
}
