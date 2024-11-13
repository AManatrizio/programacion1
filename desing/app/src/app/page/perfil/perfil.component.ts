import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { UsuariosService } from '../../services/usuarios.service';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrl: './perfil.component.css',
})
export class PerfilComponent {
  constructor(private usuariosService: UsuariosService) {}
  user: any;
  arrayUsuarios: any[] = [];
  filteredUsers: any[] = [];

  currentPage = 1;
  perPage = 4;
  totalPages = 1;
  searchQuery: string = '';

  ngOnInit() {
    const userRole = localStorage.getItem('rol');

    if (
      userRole === 'admin' ||
      userRole === 'user' ||
      userRole === 'librarian'
    ) {
      this.usuariosService.getProfile().subscribe(
        (rta: any) => {
          this.user = rta;
        },
        (error) => {
          console.error(
            'Error al obtener el perfil del usuario actual:',
            error
          );
        }
      );
    }
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
        console.error('Error al obtener usuarios desde el backend:', error);
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
    const searchQueryLowerCase = this.searchQuery.trim().toLowerCase();
    console.log('buscar: ', searchQueryLowerCase);
    this.filteredUsers = this.arrayUsuarios.filter((user) =>
      user.id.toLowerCase().includes(searchQueryLowerCase)
    );
  }

  get is_admin() {
    return localStorage.getItem('rol') === 'admin';
  }

  get is_librarian() {
    return localStorage.getItem('rol') === 'librarian';
  }

  get is_user() {
    return localStorage.getItem('rol') === 'user';
  }
}
