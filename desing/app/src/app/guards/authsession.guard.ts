import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';

export const authsessionGuard: CanActivateFn = (route, state) => {
  const router: Router = inject(Router);
  const token = localStorage.getItem('token');
  const rol = localStorage.getItem('rol');

  // Verifica si el token existe
  if (!token) {
    router.navigateByUrl('home');
    return false;
  }

  // Rutas restringidas para admin
  const restrictedRoutesForAdmin = ['mybooks', 'myloans'];

  // Verifica si el rol es admin y si la ruta a la que intenta acceder está restringida
  if (
    rol === 'admin' &&
    restrictedRoutesForAdmin.includes(route.routeConfig?.path || '')
  ) {
    router.navigateByUrl('home'); // O la ruta a la que quieras redirigir
    return false;
  }

  const restrictedRoutesForUsers = ['allloans', 'allemployees', 'allusers'];

  if (
    rol === 'user' &&
    restrictedRoutesForUsers.includes(route.routeConfig?.path || '')
  ) {
    router.navigateByUrl('home'); // O la ruta a la que quieras redirigir
    return false;
  }

  const restrictedRoutesForBibliotecary = [
    'mybooks',
    'allemployees',
    'myloans',
  ];

  if (
    rol === 'bibliotecary' &&
    restrictedRoutesForUsers.includes(route.routeConfig?.path || '')
  ) {
    router.navigateByUrl('home'); // O la ruta a la que quieras redirigir
    return false;
  }

  // Permitir el acceso si el token está presente y el rol no es admin o la ruta no está restringida
  return true;
};
