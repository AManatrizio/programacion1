import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { LoansService } from '../../services/loans.service';
import { HttpClient } from '@angular/common/http';
import { OpinionsService } from '../../services/opinions.service';

@Component({
  selector: 'app-editopinion',
  templateUrl: './editopinion.component.html',
  styleUrl: './editopinion.component.css',
})
export class EditopinionComponent {
  comentario: string = '';
  valoracion: number = 1;
  prestamoId: number = 0;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private opinionsService: OpinionsService
  ) {}

  ngOnInit(): void {
    const idParam = this.route.snapshot.paramMap.get('prestamo_id');
    console.log('ID de préstamo recibido:', idParam);
    if (idParam !== null) {
      this.prestamoId = +idParam;
      console.log('ID de préstamo convertido:', this.prestamoId);
      this.cargarOpinion();
    } else {
      console.error('ID de préstamo no válido');
    }
  }

  cargarOpinion(): void {
    this.opinionsService.getOpinionByLoanId(this.prestamoId).subscribe(
      (opinion: any) => {
        console.log('Opinión recibida:', opinion);
        this.comentario = opinion.comentario || '';
        this.valoracion = opinion.valoracion || 1;
      },
      (error) => {
        console.error('Error al cargar la opinión:', error);
      }
    );
  }

  guardarOpinion(): void {
    const opinionActualizada = {
      comentario: this.comentario,
      valoracion: this.valoracion,
    };

    this.opinionsService
      .updateOpinion(this.prestamoId, opinionActualizada)
      .subscribe(
        () => {
          alert('Opinión actualizada exitosamente.');
          this.router.navigate(['/myloans']);
        },
        (error) => {
          console.error('Error al actualizar la opinión:', error);
        }
      );
  }
}
