import { Component, Input } from '@angular/core';
import { OpinionsService } from '../../services/opinions.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-resena',
  templateUrl: './resena.component.html',
  styleUrl: './resena.component.css',
})
export class ResenaComponent {
  prestamo_id: number = 0;
  comentario: string = '';
  valoracion: number = 1;

  constructor(
    private opinionsService: OpinionsService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.prestamo_id = +params['prestamo_id'];
      console.log('Prestamo ID obtenido:', this.prestamo_id);
    });
  }

  addOpinion(): void {
    if (this.comentario && this.valoracion >= 1 && this.valoracion <= 5) {
      const opinionData = {
        comentario: this.comentario,
        valoracion: this.valoracion,
      };

      this.opinionsService.addOpinion(this.prestamo_id, opinionData).subscribe(
        (response) => {
          console.log('Opinión agregada exitosamente:', response);
          this.router.navigate(['/myloans']);
        },
        (error) => {
          console.error('Error al agregar la opinión:', error);
        }
      );
    } else {
      console.log('Por favor, completa todos los campos correctamente.');
    }
  }
}
