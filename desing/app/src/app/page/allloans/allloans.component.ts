import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LoansService } from '../../services/loans.service';

@Component({
  selector: 'app-allloans',
  templateUrl: './allloans.component.html',
  styleUrl: './allloans.component.css',
})
export class AllloansComponent {
  currentPage = 1;
  perPage = 5;
  totalPages = 1;
  searchQuery: string = '';

  loans: any[] = [];

  arrayPrestamos: any[] = [];

  filteredPrestamos: any[] = [];

  constructor(private router: Router, private loansService: LoansService) {}

  ngOnInit() {
    this.loadAllLoans();
  }

  loadAllLoans() {
    this.loansService.getLoans(this.currentPage, this.perPage).subscribe(
      (rta: any) => {
        console.log('Respuesta del API:', rta);
        this.arrayPrestamos = rta.prestamos || [];
        this.filteredPrestamos = [...this.arrayPrestamos];
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
      this.loadAllLoans();
    }
  }

  editarprestamo(loan: any) {
    console.log('Estoy editando', loan);
    this.router.navigate(['/prestamo/' + loan.id + '/Editar']);
  }

  buscar() {
    console.log('buscar: ', this.searchQuery);
    this.filteredPrestamos = this.arrayPrestamos.filter((loans) =>
      loans.id.includes(this.searchQuery)
    );
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

  deleteLoan(id: number) {
    if (confirm('¿Estás seguro de que deseas eliminar este préstamo?')) {
      this.loansService.deleteLoans(id).subscribe(
        () => {
          console.log(`Préstamo con id ${id} eliminado`);
          this.loadAllLoans(); // Recargar la lista después de eliminar
        },
        (error) => {
          console.error('Error al eliminar el préstamo:', error);
        }
      );
    }
  }
}
