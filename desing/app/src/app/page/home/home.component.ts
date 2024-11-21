import { Component } from '@angular/core';
import { BooksService } from '../../services/books.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
})
export class HomeComponent {
  librosMejorValorados: any[] = [];

  constructor(private libroService: BooksService) {}

  ngOnInit(): void {
    this.libroService.getLibrosMejorValorados().subscribe(
      (books) => {
        this.librosMejorValorados = books;
        console.log('Libros mejor valorados:', books); // Imprime en la consola del navegador
      },
      (error) => {
        console.error('Error al cargar libros mejor valorados:', error);
      }
    );
  }

  agruparLibros(libros: any[], cantidadPorGrupo: number): any[][] {
    const grupos = [];
    for (let i = 0; i < libros.length; i += cantidadPorGrupo) {
      grupos.push(libros.slice(i, i + cantidadPorGrupo));
    }
    return grupos;
  }
}
