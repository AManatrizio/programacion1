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

  // EL ARCHIVO .TS IMPORTA FUNCIONALIDADES DE LOS SERVICIOS Y LOS .HTML IMPORTAN FUNCIONALIDADES DE LOS .TS

  // El archivo .ts se va a definir
  irAlLogin(dataLogin: any) {
    // Suscribe: 3 estados (Next, Error, )
    this.authService.login(dataLogin).subscribe({
      next: (rta: any) => {
        alert('Credenciales correctas!!!');
        console.log('Exito: ', rta);
        // Agrega el token al Local Storage
        localStorage.setItem('token', rta.access_token);

        // Decodifica el token para obtener el valor de la clave "rol"
        const decodedToken: any = jwt_decode(rta.access_token);
        const rol = decodedToken.rol;

        // Guarda el valor de la clave "rol" en el Local Storage
        localStorage.setItem('rol', rol);
        this.router.navigateByUrl('home');
      },
      error: (err: any) => {
        alert('Usuario o contraseña incorrecta.');
        console.log('Exito: ', err);
        localStorage.removeItem('token');
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
