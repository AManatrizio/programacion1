import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LoansService } from '../../services/loans.service';

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

  constructor(private router: Router, private loansService: LoansService) {}

  ngOnInit() {
    this.loadLoans();
  }

  loadLoans() {
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
}
