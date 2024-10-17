import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UsuariosService } from '../../services/usuarios.service'; // Asegúrate de tener el servicio adecuado

@Component({
  selector: 'app-allusers',
  templateUrl: './allusers.component.html',
  styleUrls: ['./allusers.component.css'],
})
export class AllusersComponent {
  searchQuery = '';
  users: any[] = [];

  arrayUsuarios: any[] = [];

  filteredUsers: any[] = [];

  constructor(
    private router: Router,
    private usuariosService: UsuariosService
  ) {}

  ngOnInit() {
    this.usuariosService.getUsers().subscribe(
      (rta: any) => {
        console.log('Respuesta del API:', rta);
        this.arrayUsuarios = rta.usuarios || [];
        this.filteredUsers = [...this.arrayUsuarios];
      },
      (error) => {
        console.error('Error al obtener usuarios:', error);
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
