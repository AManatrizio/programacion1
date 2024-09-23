import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './page/home/home.component';
import { LoansComponent } from './page/loans/loans.component';
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


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoansComponent,
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

  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
