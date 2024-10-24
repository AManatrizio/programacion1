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
    private loansService: LoansService,
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
    this.loanId = this.route.snapshot.paramMap.get('id') || '';

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

  submit(): void {
    if (this.editLoanForm.valid) {
      this.loansService
        .updateLoan(this.loanId, this.editLoanForm.value)
        .subscribe(
          () => {
            this.router.navigate(['/allloans']);
          },
          (error) => {
            console.error('Error al actualizar el préstamo:', error);
            alert('Revisar datos ingresados');
          }
        );
    }
  }
}
