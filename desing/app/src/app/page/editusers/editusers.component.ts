import { Component } from '@angular/core';
import { BooksService } from '../../services/books.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { UsuariosService } from '../../services/usuarios.service';
@Component({
  selector: 'app-editusers',
  templateUrl: './editusers.component.html',
  styleUrl: './editusers.component.css',
})
export class EditusersComponent {
  editUsersForm: FormGroup;
  userId: any;

  constructor(
    private fb: FormBuilder,
    private usuariosService: UsuariosService,
    private route: ActivatedRoute,
    private router: Router
  ) {
    this.editUsersForm = this.fb.group({
      nombre: ['', Validators.required],
      telefono: ['', Validators.required],
      email: ['', Validators.required],
      rol: ['', Validators.required],
    });
  }

  ngOnInit(): void {
    this.userId = this.route.snapshot.paramMap.get('id') || '';

    this.usuariosService.getUserById(this.userId).subscribe((user) => {
      this.editUsersForm.patchValue({
        nombre: user.nombre,
        telefono: user.telefono,
        email: user.email,
        rol: user.rol,
      });
    });
  }

  submit(): void {
    if (this.editUsersForm.valid) {
      this.usuariosService
        .updateUser(this.userId, this.editUsersForm.value)
        .subscribe(
          () => {
            this.router.navigate(['/allusers']);
          },
          (error) => {
            console.error('Error al actualizar el préstamo:', error);
            alert('Revisar datos ingresados');
          }
        );
    }
  }
}
