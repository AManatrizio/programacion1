import { BooksService } from '../../services/books.service';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-addbooks',
  templateUrl: './addbooks.component.html',
  styleUrl: './addbooks.component.css',
})
export class AddbooksComponent {
  addBooksForms!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private booksService: BooksService,
    private router: Router
  ) {
    this.addBooksForms = this.formBuilder.group({
      nombre: ['', Validators.required],
      genero: ['', [Validators.required]],
      imagen_url: ['', [Validators.required]],
    });
  }

  submit() {
    if (this.addBooksForms.valid) {
      console.log(
        'Datos del formulario de registro: ',
        this.addBooksForms.value
      );

      this.booksService.addBooks(this.addBooksForms.value).subscribe({
        next: (response: any) => {
          console.log('Respuesta del servidor: ', response);
          alert('Libro creado exitosamente');
          this.router.navigateByUrl('/allbooks');
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
