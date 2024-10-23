import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import jwt_decode from 'jwt-decode';
import 'jwt-decode';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
})
export class LoginComponent {
  loginForm!: FormGroup;

  constructor(
    private authService: AuthService,
    private router: Router,
    private formBuilder: FormBuilder
  ) {
    this.loginForm = this.formBuilder.group({
      email: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  irAlLogin(dataLogin: any) {
    this.authService.login(dataLogin).subscribe({
      next: (rta: any) => {
        alert('Credenciales correctas!!!');
        console.log('Exito: ', rta);

        const decodedToken: any = jwt_decode(rta.access_token);
        const rol = decodedToken.rol;

        localStorage.setItem('rol', rol);
        localStorage.setItem('token', rta.access_token);
        this.router.navigateByUrl('home');
      },
      error: (err: any) => {
        alert('Usuario o contraseña incorrecta.');
        console.log('Exito: ', err);
        localStorage.removeItem('token');
        localStorage.removeItem('rol');
      },
      complete: () => {
        console.log('Fianlizo');
      },
    });
  }

  submit() {
    if (this.loginForm.valid) {
      console.log('Datos del formulario: ', this.loginForm.value);
      this.irAlLogin(this.loginForm.value);
    } else {
      alert('Los valores son requeridos');
    }
  }
}
