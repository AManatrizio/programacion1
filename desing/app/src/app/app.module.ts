import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './page/home/home.component';
import { ErrorPageComponent } from './page/error-page/error-page.component';

import { FooterComponent } from './components/footer/footer.component';
import { NavbarComponent } from './components/navbar/navbar.component';

import { LoginComponent } from './page/login/login.component';
import { SinginComponent } from './page/singin/singin.component';
import { WelcomeComponent } from './page/welcome/welcome.component';
import { ResenaComponent } from './page/resena/resena.component';
import { MenuComponent } from './page/menu/menu.component';
import { MyloansComponent } from './page/myloans/myloans.component';
import { AllloansComponent } from './page/allloans/allloans.component';
import { AllemployeesComponent } from './page/allemployees/allemployees.component';
import { AllusersComponent } from './page/allusers/allusers.component';
import { NavbarBackHomeComponent } from './components/navbar-back-home/navbar-back-home.component';
import { AllbooksComponent } from './page/allbooks/allbooks.component';
import { PerfilComponent } from './page/perfil/perfil.component';
import { LoginadminComponent } from './page/loginadmin/loginadmin.component';
import { NavbaradminComponent } from './components/navbaradmin/navbaradmin.component';
import { MybooksComponent } from './page/mybooks/mybooks.component';
import { ResenaadminComponent } from './page/resenaadmin/resenaadmin.component';
import { NavbarBackHomeAdminComponent } from './components/navbar-back-home-admin/navbar-back-home-admin.component';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ErrorPageComponent,

    FooterComponent,
    NavbarComponent,

    LoginComponent,
    SinginComponent,
    WelcomeComponent,
    ResenaComponent,
    MenuComponent,
    MyloansComponent,
    AllloansComponent,
    AllemployeesComponent,
    AllusersComponent,
    NavbarBackHomeComponent,
    AllbooksComponent,
    PerfilComponent,
    LoginadminComponent,
    NavbaradminComponent,
    MybooksComponent,
    ResenaadminComponent,
    NavbarBackHomeAdminComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
