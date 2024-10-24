import { Component } from '@angular/core';
import { BooksService } from './../../services/books.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-editbooks',
  templateUrl: './editbooks.component.html',
  styleUrl: './editbooks.component.css',
})
export class EditbooksComponent {
  editBooksForm: FormGroup;
  booksId: any;

  constructor(
    private fb: FormBuilder,
    private booksService: BooksService,
    private route: ActivatedRoute,
    private router: Router
  ) {
    this.editBooksForm = this.fb.group({
      nombre: ['', Validators.required],
      genero: ['', Validators.required],
      imagen_url: ['', Validators.required],
    });
  }

  ngOnInit(): void {
    this.booksId = this.route.snapshot.paramMap.get('id') || '';

    this.booksService.getBooksById(this.booksId).subscribe((book) => {
      this.editBooksForm.patchValue({
        nombre: book.nombre,
        genero: book.genero,
        imagen_url: book.imagen_url,
      });
    });
  }

  submit(): void {
    if (this.editBooksForm.valid) {
      this.booksService
        .updateBooks(this.booksId, this.editBooksForm.value)
        .subscribe(
          () => {
            this.router.navigate(['/allbooks']);
          },
          (error) => {
            console.error('Error al actualizar el préstamo:', error);
            alert('Revisar datos ingresados');
          }
        );
    }
  }
}
