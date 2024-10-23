import { Component } from '@angular/core';
import { BooksService } from './../../services/books.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { LoansService } from '../../services/loans.service';

@Component({
  selector: 'app-editloans',
  templateUrl: './editloans.component.html',
  styleUrl: './editloans.component.css',
})
export class EditloansComponent {
  editLoanForm: FormGroup;
  loanId: any;

  constructor(
    private fb: FormBuilder,
    private loansService: LoansService, // Servicio para interactuar con el backend
    private route: ActivatedRoute,
    private router: Router
  ) {
    this.editLoanForm = this.fb.group({
      prestamo: ['', Validators.required],
      fecha_inicio: ['', Validators.required],
      fecha_vencimiento: ['', Validators.required],
      usuario_id: ['', Validators.required],
      libro_id: ['', Validators.required],
    });
  }

  ngOnInit(): void {
    // Obtener el ID del préstamo desde la URL
    this.loanId = this.route.snapshot.paramMap.get('id') || '';

    // Cargar los datos del préstamo existente
    this.loansService.getLoanById(this.loanId).subscribe((loan) => {
      this.editLoanForm.patchValue({
        prestamo: loan.prestamo,
        fecha_inicio: loan.fecha_inicio,
        fecha_vencimiento: loan.fecha_vencimiento,
        usuario_id: loan.usuario_id,
        libro_id: loan.libro_id,
      });
    });
  }

  // Función para enviar el formulario
  submit(): void {
    if (this.editLoanForm.valid) {
      this.loansService
        .updateLoan(this.loanId, this.editLoanForm.value)
        .subscribe(() => {
          // Redirigir o mostrar un mensaje de éxito
          this.router.navigate(['/loans']); // Redirigir a la página de lista de préstamos
        });
    }
  }
}
