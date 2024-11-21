import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { LoansService } from '../../services/loans.service';
import { UsuariosService } from '../../services/usuarios.service';
import { BooksService } from '../../services/books.service';
import { Component } from '@angular/core';

@Component({
  selector: 'app-allbooks',
  templateUrl: './allbooks.component.html',
  styleUrl: './allbooks.component.css',
})
export class AllbooksComponent {
  arrayLibros = [];
  filteredBooks = [];
  searchQuery: string = '';
  currentPage: number = 1;
  searchField: string = 'nombre';
  perPage: number = 4;
  totalPages: number = 1;
  book: any = {};

  constructor(
    private booksService: BooksService,
    private router: Router,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    this.loadBooks();
  }

  loadBooks() {
    this.booksService
      .getBooks(
        this.currentPage,
        this.perPage,
        this.searchField,
        this.searchQuery
      )
      .subscribe(
        (rta: any) => {
          console.log('Respuesta del API:', rta);
          this.arrayLibros = rta.libros || [];
          this.filteredBooks = [...this.arrayLibros];
          this.totalPages = rta.pages;
        },
        (error) => {
          console.error('Error al obtener libros:', error);
        }
      );
  }

  changePage(page: number, event: Event) {
    event.preventDefault();

    if (page > 0 && page <= this.totalPages) {
      this.currentPage = page;
      this.loadBooks();
    }
  }

  buscar() {
    this.currentPage = 1;
    this.loadBooks();
  }

  deleteBook(id: number) {
    if (confirm('¿Estás seguro de que deseas eliminar este libro?')) {
      this.booksService.deleteBooks(id).subscribe(
        () => {
          console.log(`Libro con id ${id} eliminado`);
          this.loadBooks();
        },
        (error) => {
          console.error('Error al eliminar el libro:', error);
        }
      );
    }
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
  verResenas(libroId: number) {
    this.router.navigate(['/resenas/libro', libroId]);
  }
}
