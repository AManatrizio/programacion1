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

  currentPage = 1;
  perPage = 5;
  totalPages = 1;
  searchQuery: string = '';

  constructor(private usuariosService: UsuariosService) {}

  ngOnInit() {
    this.loadUsers();
  }

  loadUsers() {
    this.usuariosService.getUsers(this.currentPage, this.perPage).subscribe(
      (rta: any) => {
        console.log('Respuesta del API:', rta);
        this.arrayUsuarios = rta.usuarios || [];
        this.filteredUsers = [...this.arrayUsuarios];
        this.totalPages = rta.pages;
      },
      (error) => {
        console.error('Error al obtener usuarios:', error);
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
    this.filteredUsers = this.arrayUsuarios.filter((user) =>
      user.nombre.toLowerCase().includes(this.searchQuery.toLowerCase())
    );
  }

  editarusuario(user: any) {
    console.log('Editando usuario:', user);
  }

  eliminarUsuario(id: number) {
    console.log('Eliminando usuario con ID:', id);
  }

  get admin_and_bibliotecary() {
    return (
      localStorage.getItem('rol') === 'admin' ||
      localStorage.getItem('rol') === 'bibliotecary'
    );
  }

  get is_admin() {
    return localStorage.getItem('rol') === 'admin';
  }
}
