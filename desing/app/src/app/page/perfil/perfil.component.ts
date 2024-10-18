import { Component } from '@angular/core';
import { UsuariosService } from '../../services/usuarios.service';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrl: './perfil.component.css',
})
export class PerfilComponent {
  constructor(private usuariosService: UsuariosService) {}
  user: any;

  ngOnInit(): void {
    this.usuariosService.getProfile().subscribe(
      (rta: any) => {
        console.log('Respuesta del API:', rta);
        this.user = rta;
      },
      (error) => {
        console.error('Error al obtener el perfil:', error);
      }
    );
  }
}
