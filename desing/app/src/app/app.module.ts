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

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoansComponent,
    ErrorPageComponent,
    FooterComponent,
    NavbarComponent,
    LoginComponent,
    SinginComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
