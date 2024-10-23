import { Component } from '@angular/core';
import { BooksService } from './../../services/books.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoansService } from '../../services/loans.service';

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
    private router: Router
  ) {
    this.addLoansForms = this.formBuilder.group({
      prestamo: ['', Validators.required],
      fecha_inicio: ['', [Validators.required]],
      fecha_vencimiento: ['', [Validators.required]],
      usuario_id: ['', [Validators.required]],
      libro_id: ['', [Validators.required]],
    });
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
          alert('Lo ingresado es invalido');
        },
      });
    } else {
      alert('Revise los campos ingresados, ya que son incorrectos');
    }
  }
}
