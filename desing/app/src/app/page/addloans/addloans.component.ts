import { Component } from '@angular/core';
import { BooksService } from '../../services/books.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { LoansService } from '../../services/loans.service';
import { UsuariosService } from '../../services/usuarios.service';

@Component({
  selector: 'app-addloans',
  templateUrl: './addloans.component.html',
  styleUrl: './addloans.component.css',
})
export class AddloansComponent {
  addLoansForms!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private loansService: LoansService,
    private usuarioService: UsuariosService,
    private router: Router,
    private route: ActivatedRoute
  ) {
    this.addLoansForms = this.formBuilder.group({
      fecha_inicio: ['', [Validators.required]],
      fecha_vencimiento: ['', [Validators.required]],
      usuario_id: ['', [Validators.required]],
      libro_id: ['', [Validators.required]],
    });
  }
  ngOnInit(): void {
    const libroId = this.route.snapshot.paramMap.get('id');
    if (libroId) {
      this.addLoansForms.patchValue({ libro_id: libroId });
    }

    const fechaActual = new Date();
    const fechaVencimiento = new Date();
    fechaVencimiento.setDate(fechaActual.getDate() + 21);

    const formatearFecha = (fecha: Date): string => {
      const dia = String(fecha.getDate()).padStart(2, '0');
      const mes = String(fecha.getMonth() + 1).padStart(2, '0');
      const año = fecha.getFullYear();
      return `${dia}/${mes}/${año}`;
    };

    this.addLoansForms.patchValue({
      fecha_inicio: formatearFecha(fechaActual),
      fecha_vencimiento: formatearFecha(fechaVencimiento),
    });

    this.loadUsers();
  }

  submit() {
    if (this.addLoansForms.valid) {
      console.log(
        'Datos del formulario de registro: ',
        this.addLoansForms.value
      );

      this.loansService.addLoans(this.addLoansForms.value).subscribe({
        next: (response: any) => {
          console.log('Respuesta del servidor: ', response);
          alert('Prestamo creado exitosamente');
          this.router.navigateByUrl('/allloans');
        },
        error: (err: any) => {
          console.error('Error en la solicitud de registro: ', err);
          alert(
            'Lo ingresado es inválido. Por favor, revise los datos e intente nuevamente.'
          );
        },
      });
    } else {
      alert('Revise los campos ingresados, ya que son incorrectos');
    }
  }

  usuarios: any[] = [];

  loadUsers(): void {
    this.usuarioService.getUsers(1, 100).subscribe(
      (data: any) => {
        console.log('Datos obtenidos:', data);
        if (data.usuarios) {
          this.usuarios = data.usuarios.filter(
            (usuario: any) => usuario.rol === 'user'
          );
        } else {
          this.usuarios = [];
        }
      },
      (error) => {
        console.error('Error al obtener los usuarios:', error);
      }
    );
  }
}
