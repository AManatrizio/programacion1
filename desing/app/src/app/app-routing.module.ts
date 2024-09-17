import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './page/home/home.component';
import { LoansComponent } from './page/loans/loans.component';
import { ErrorPageComponent } from './page/error-page/error-page.component';
import { LoginComponent } from './page/login/login.component';
import { SinginComponent } from './page/singin/singin.component';

const routes: Routes = [
  { path: 'home' , component: HomeComponent},
  { path: '', redirectTo: 'home', pathMatch: 'full' },

  { path: 'loans' , component: LoansComponent},

  { path: 'login', component: LoginComponent},

  { path: 'singin', component: SinginComponent},

  { path: '**', redirectTo: 'error_page'},
  { path: 'error_page', component: ErrorPageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
