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
import { PerfiluserComponent } from './page/perfiluser/perfiluser.component';
import { LoginadminComponent } from './page/loginadmin/loginadmin.component';
import { HomeadminComponent } from './page/homeadmin/homeadmin.component';
import { MenuusuarioComponent } from './page/menuusuario/menuusuario.component';
import { MybooksComponent } from './page/mybooks/mybooks.component';
import { PerfiladminComponent } from './page/perfiladmin/perfiladmin.component';
import { MyloansComponent } from './page/myloans/myloans.component';
import { ResenaadminComponent } from './page/resenaadmin/resenaadmin.component';


const routes: Routes = [
  { path: 'home' , component: HomeComponent},
  { path: '', redirectTo: 'welcome', pathMatch: 'full' },


  { path: 'login', component: LoginComponent},

  { path: 'singin', component: SinginComponent},

  { path: 'welcome', component: WelcomeComponent},

  { path: 'resena', component:  ResenaComponent},

  { path: 'menu', component: MenuComponent},

  { path: 'allloans', component: AllloansComponent},

  { path: 'allemployees', component: AllemployeesComponent},

  { path: 'allusers', component: AllusersComponent},

  { path: 'allbooks', component: AllbooksComponent},

  { path: 'perfil', component: PerfiluserComponent},

  { path: 'loginadmin', component: LoginadminComponent},

  { path: 'homeadmin', component: HomeadminComponent},

  { path: 'menuusuario', component: MenuusuarioComponent},

  { path: 'mybooks', component: MybooksComponent},

  { path: 'perfiladmin', component: PerfiladminComponent},

  { path: 'myloans', component: MyloansComponent},

  { path: 'resenaadmin', component: ResenaadminComponent},

  { path: '**', redirectTo: 'error_page'},
  { path: 'error_page', component: ErrorPageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
