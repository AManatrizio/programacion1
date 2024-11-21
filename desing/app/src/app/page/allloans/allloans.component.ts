import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LoansService } from '../../services/loans.service';

@Component({
  selector: 'app-allloans',
  templateUrl: './allloans.component.html',
  styleUrl: './allloans.component.css',
})
export class AllloansComponent {
  arrayPrestamos: any[] = [];
  filteredPrestamos: any[] = [];
  searchQuery: string = '';
  searchField: string = 'usuario_id';
  currentPage: number = 1;
  perPage: number = 4;
  totalPages: number = 1;

  loans: any[] = [];

  constructor(private loansService: LoansService) {}

  ngOnInit() {
    this.loadAllLoans();
  }

  loadAllLoans() {
    this.loansService
      .getLoans(
        this.currentPage,
        this.perPage,
        this.searchField,
        this.searchQuery
      )
      .subscribe(
        (rta: any) => {
          console.log('Respuesta del API:', rta);
          this.arrayPrestamos = rta.prestamos || [];
          this.filteredPrestamos = [...this.arrayPrestamos];
          this.totalPages = rta.pages;
        },
        (error) => {
          console.error('Error al obtener prestamos:', error);
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

  buscar() {
    this.currentPage = 1;
    this.loadAllLoans();
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

  deleteLoan(id: number) {
    if (confirm('¿Estás seguro de que deseas eliminar este préstamo?')) {
      this.loansService.deleteLoans(id).subscribe(
        () => {
          console.log(`Préstamo con id ${id} eliminado`);
          this.loadAllLoans();
        },
        (error) => {
          console.error('Error al eliminar el préstamo:', error);
        }
      );
    }
  }
}
