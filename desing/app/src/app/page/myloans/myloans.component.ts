import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LoansService } from '../../services/loans.service';
import { OpinionsService } from '../../services/opinions.service';

@Component({
  selector: 'app-myloans',
  templateUrl: './myloans.component.html',
  styleUrl: './myloans.component.css',
})
export class MyloansComponent {
  loans: any[] = [];

  arrayPrestamos: any[] = [];

  filteredPrestamos: any[] = [];

  currentPage = 1;
  perPage = 4;
  totalPages = 1;
  searchQuery: string = '';
  prestamosConOpiniones: number[] = [];
  opinionesUsuario: { [prestamoId: number]: any } = {};

  constructor(
    private router: Router,
    private loansService: LoansService,
    private opinionesService: OpinionsService
  ) {}

  ngOnInit() {
    this.loadLoans();
    this.loadOpiniones();
  }

  loadLoans() {
    this.loansService.getLoans(this.currentPage, this.perPage).subscribe(
      (rta: any) => {
        console.log('Respuesta del API:', rta);
        this.arrayPrestamos = rta.prestamos || [];
        this.filteredPrestamos = [...this.arrayPrestamos];
        this.totalPages = rta.pages;

        // Verificar estructura de los datos cargados
        console.log('Prestamos cargados:', this.arrayPrestamos);
      },
      (error) => {
        console.error('Error al obtener préstamos:', error);
      }
    );
  }
  changePage(page: number, event: Event) {
    event.preventDefault();

    if (page > 0 && page <= this.totalPages) {
      this.currentPage = page;
      this.loadLoans();
    }
  }

  editarprestamo(loan: any) {
    console.log('Estoy editando', loan);
    this.router.navigate(['/prestamo/' + loan.id + '/Editar']);
  }

  buscar() {
    const searchQueryLowerCase = this.searchQuery.trim().toLowerCase();
    console.log('buscar: ', searchQueryLowerCase);
    this.filteredPrestamos = this.arrayPrestamos.filter((loan) =>
      loan.id.toLowerCase().includes(searchQueryLowerCase)
    );
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

  loadOpiniones(): void {
    this.opinionesService.getOpinionesByUser().subscribe(
      (response: any) => {
        console.log('Respuesta del servicio:', response);

        if (Array.isArray(response.opiniones)) {
          // Crear un mapa de opiniones por prestamo_id
          this.opinionesUsuario = response.opiniones.reduce(
            (map: any, opinion: any) => {
              map[opinion.prestamo_id] = opinion;
              return map;
            },
            {}
          );

          console.log('Mapa de opiniones cargado:', this.opinionesUsuario);
        } else {
          console.error('La respuesta no es un array:', response);
        }
      },
      (error) => {
        console.error('Error al cargar opiniones del usuario:', error);
      }
    );
  }

  tieneOpinion(prestamoId: number): boolean {
    return this.opinionesUsuario.hasOwnProperty(prestamoId);
  }

  obtenerOpinion(prestamoId: number): any {
    return this.opinionesUsuario[prestamoId];
  }
}
