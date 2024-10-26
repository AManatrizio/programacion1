import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UsuariosService } from '../../services/usuarios.service';
@Component({
  selector: 'app-allusers',
  templateUrl: './allusers.component.html',
  styleUrls: ['./allusers.component.css'],
})
export class AllusersComponent {
  arrayUsuarios: any[] = [];
  filteredUsers: any[] = [];

  searchQuery: string = '';
  searchField: string = 'nombre';
  currentPage: number = 1;
  perPage: number = 5;
  totalPages: number = 1;

  constructor(private usuariosService: UsuariosService) {}

  users: any[] = [];

  ngOnInit() {
    this.loadUsers();
  }

  loadUsers() {
    this.usuariosService
      .getUsers(
        this.currentPage,
        this.perPage,
        this.searchField,
        this.searchQuery
      )
      .subscribe(
        (rta: any) => {
          console.log('Respuesta del API:', rta);
          this.arrayUsuarios = rta.usuarios || [];
          this.filteredUsers = [...this.arrayUsuarios];
          this.totalPages = rta.pages;
        },
        (error) => {
          console.error('Error al obtener prestamos:', error);
        }
      );
  }

  changePage(page: number, event: Event) {
    event.preventDefault();

    if (page > 0 && page <= this.totalPages) {
      this.currentPage = page;
      this.loadUsers();
    }
  }

  buscar() {
    this.currentPage = 1;
    this.loadUsers();
  }

  editarusuario(user: any) {
    console.log('Editando usuario:', user);
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
  deleteUsers(id: number) {
    if (confirm('¿Estás seguro de que deseas eliminar este usuario?')) {
      this.usuariosService.deleteUsers(id).subscribe(
        () => {
          console.log(`Usuario con id ${id} eliminado`);
          this.loadUsers();
        },
        (error) => {
          console.error('Error al eliminar el usuario:', error);
        }
      );
    }
  }
}
