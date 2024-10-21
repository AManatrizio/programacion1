import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-singin',
  templateUrl: './singin.component.html',
  styleUrls: ['./singin.component.css'],
})
export class SinginComponent {
  signupForm!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    this.signupForm = this.formBuilder.group(
      {
        nombre: ['', Validators.required],
        telefono: ['', [Validators.required, Validators.minLength(10)]],
        email: ['', [Validators.required, Validators.email]],
        password: ['', [Validators.required, Validators.minLength(3)]],
        confirmPassword: ['', Validators.required],
      },
      { validator: this.passwordMatchValidator }
    );
  }

  submit() {
    if (this.signupForm.valid) {
      console.log('Datos del formulario de registro: ', this.signupForm.value);

      this.authService.signup(this.signupForm.value).subscribe({
        next: (response: any) => {
          console.log('Respuesta del servidor: ', response);
          alert('Usuario creado exitosamente');
          this.router.navigateByUrl('/login');
        },
        error: (err: any) => {
          console.error('Error en la solicitud de registro: ', err);
          alert('El mail ingresado es invalido');
        },
      });
    } else {
      alert('Revise los campos ingresados, ya que son incorrectos');
    }
  }

  passwordMatchValidator(formGroup: FormGroup) {
    const password = formGroup.get('password')?.value;
    const confirmPassword = formGroup.get('confirmPassword')?.value;

    return password === confirmPassword ? null : { mismatch: true };
  }
}
