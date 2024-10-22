import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';

export const authsessionGuard: CanActivateFn = (route, state) => {
  const router: Router = inject(Router);
  const token = localStorage.getItem('token');
  const rol = localStorage.getItem('rol');

  if (!token) {
    router.navigateByUrl('home');
    return false;
  }

  const restrictedRoutesForAdmin = ['mybooks', 'myloans'];

  if (
    rol === 'admin' &&
    restrictedRoutesForAdmin.includes(route.routeConfig?.path || '')
  ) {
    router.navigateByUrl('home');
  }

  const restrictedRoutesForUsers = [
    'allloans',
    'allemployees',
    'allusers',
    'libros/addbooks',
    'prestamos/addloans',
  ];

  if (
    rol === 'user' &&
    restrictedRoutesForUsers.includes(route.routeConfig?.path || '')
  ) {
    router.navigateByUrl('home');
    return false;
  }

  const restrictedRoutesForBibliotecary = [
    'mybooks',
    'allemployees',
    'myloans',
  ];

  if (
    rol === 'bibliotecary' &&
    restrictedRoutesForBibliotecary.includes(route.routeConfig?.path || '')
  ) {
    router.navigateByUrl('home');
  }
  return true;
};
