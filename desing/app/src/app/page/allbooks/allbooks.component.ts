import { Component } from '@angular/core';
import { BooksService } from '../../services/books.service';

@Component({
  selector: 'app-allbooks',
  templateUrl: './allbooks.component.html',
  styleUrl: './allbooks.component.css',
})
export class AllbooksComponent {
  arrayLibros: any[] = [];
  filteredBooks: any[] = [];

  currentPage = 1;
  perPage = 5;
  totalPages = 1;
  searchQuery: string = '';

  constructor(private booksService: BooksService) {}

  ngOnInit() {
    this.loadBooks();
  }

  loadBooks() {
    this.booksService.getBooks(this.currentPage, this.perPage).subscribe(
      (rta: any) => {
        console.log('Respuesta del API:', rta);
        this.arrayLibros = rta.libros || [];
        this.filteredBooks = [...this.arrayLibros];
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
      this.loadBooks();
    }
  }

  buscar() {
    this.filteredBooks = this.arrayLibros.filter((book) =>
      book.nombre.toLowerCase().includes(this.searchQuery.toLowerCase())
    );
  }

  editarlibro(book: any) {
    console.log('Editando usuario:', book);
  }

  deleteBook(id: number) {
    if (confirm('¿Estás seguro de que deseas eliminar este préstamo?')) {
      this.booksService.deleteBooks(id).subscribe(
        () => {
          console.log(`Libro con id ${id} eliminado`);
          this.loadBooks(); // Recargar la lista después de eliminar
        },
        (error) => {
          console.error('Error al eliminar el libro:', error);
        }
      );
    }
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
