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
import { MyloansComponent } from './page/myloans/myloans.component';
import { EditopinionComponent } from './page/editopinion/editopinion.component';
import { authsessionGuard } from './guards/authsession.guard';
import { AddbooksComponent } from './page/addbooks/addbooks.component';
import { AddloansComponent } from './page/addloans/addloans.component';
import { EditloansComponent } from './page/editloans/editloans.component';
import { EditusersComponent } from './page/editusers/editusers.component';
import { EditbooksComponent } from './page/editbooks/editbooks.component';
import { AllresenalibroComponent } from './page/allresenalibro/allresenalibro.component';

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
    path: 'libros/addbooks',
    component: AddbooksComponent,
    canActivate: [authsessionGuard],
  },
  {
    path: 'prestamo/editloans/:id',
    component: EditloansComponent,
    canActivate: [authsessionGuard],
  },
  {
    path: 'usuario/editusers/:id',
    component: EditusersComponent,
    canActivate: [authsessionGuard],
  },
  {
    path: 'libro/editbooks/:id',
    component: EditbooksComponent,
    canActivate: [authsessionGuard],
  },
  {
    path: 'prestamos/addloans/:id',
    component: AddloansComponent,
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
    path: 'myloans',
    component: MyloansComponent,
    canActivate: [authsessionGuard],
  },

  {
    path: 'opiniones/addopinion/:prestamo_id',
    component: ResenaComponent,
  },

  { path: 'resenas/libro/:id', component: AllresenalibroComponent },

  {
    path: 'opinion/editopinion/:prestamo_id',
    component: EditopinionComponent,
  },

  { path: 'usuarios/me', component: PerfilComponent },

  { path: '**', redirectTo: 'error_page' },
  { path: 'error_page', component: ErrorPageComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
