import { Component } from '@angular/core';
import { OpinionsService } from '../../services/opinions.service';
import { ActivatedRoute } from '@angular/router';
import { BooksService } from '../../services/books.service';

@Component({
  selector: 'app-allresenalibro',
  templateUrl: './allresenalibro.component.html',
  styleUrl: './allresenalibro.component.css',
})
export class AllresenalibroComponent {
  libroId: number = 0;
  resenas: any[] = [];

  constructor(
    private route: ActivatedRoute,
    private resenasService: OpinionsService
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.libroId = +params['id'];
      this.cargarReseñas();
    });
  }

  cargarReseñas(): void {
    this.resenasService.getResenasByLibroId(this.libroId).subscribe(
      (resenas: any[]) => {
        this.resenas = resenas;
        console.log('Reseñas obtenidas:', this.resenas);
      },
      (error) => {
        console.error('Error al cargar las reseñas:', error);
      }
    );
  }
}
