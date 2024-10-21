import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './page/home/home.component';
import { ErrorPageComponent } from './page/error-page/error-page.component';
import { LoginComponent } from './page/login/login.component';
import { SinginComponent } from './page/singin/singin.component';
import { WelcomeComponent } from './page/welcome/welcome.component';
import { ResenaComponent } from './page/resena/resena.component';
import { MenuComponent } from './page/menu/menu.component';
import { AllloansComponent } from './page/allloans/allloans.component';
import { AllemployeesComponent } from './page/allemployees/allemployees.component';
import { AllusersComponent } from './page/allusers/allusers.component';
import { AllbooksComponent } from './page/allbooks/allbooks.component';
import { PerfilComponent } from './page/perfil/perfil.component';
import { LoginadminComponent } from './page/loginadmin/loginadmin.component';
import { MybooksComponent } from './page/mybooks/mybooks.component';
import { MyloansComponent } from './page/myloans/myloans.component';
import { ResenaadminComponent } from './page/resenaadmin/resenaadmin.component';
import { authsessionGuard } from './guards/authsession.guard';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: '', redirectTo: 'welcome', pathMatch: 'full' },

  { path: 'login', component: LoginComponent },

  { path: 'register', component: SinginComponent },

  { path: 'welcome', component: WelcomeComponent },

  { path: 'resena', component: ResenaComponent },

  { path: 'menu', component: MenuComponent },

  {
    path: 'allloans',
    component: AllloansComponent,
    canActivate: [authsessionGuard],
  },

  {
    path: 'allemployees',
    component: AllemployeesComponent,
    canActivate: [authsessionGuard],
  },

  {
    path: 'allusers',
    component: AllusersComponent,
    canActivate: [authsessionGuard],
  },

  {
    path: 'allbooks',
    component: AllbooksComponent,
    canActivate: [authsessionGuard],
  },

  { path: 'perfil', component: PerfilComponent },

  { path: 'loginadmin', component: LoginadminComponent },

  {
    path: 'mybooks',
    component: MybooksComponent,
    canActivate: [authsessionGuard],
  },

  {
    path: 'myloans',
    component: MyloansComponent,
    canActivate: [authsessionGuard],
  },

  { path: 'resenaadmin', component: ResenaadminComponent },

  { path: 'usuarios/me', component: PerfilComponent },

  { path: '**', redirectTo: 'error_page' },
  { path: 'error_page', component: ErrorPageComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
