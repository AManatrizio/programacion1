import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './page/home/home.component';
import { ErrorPageComponent } from './page/error-page/error-page.component';

import { FooterComponent } from './components/footer/footer.component';

import { LoginComponent } from './page/login/login.component';
import { SinginComponent } from './page/singin/singin.component';
import { WelcomeComponent } from './page/welcome/welcome.component';
import { ResenaComponent } from './page/resena/resena.component';
import { MenuComponent } from './page/menu/menu.component';
import { MyloansComponent } from './page/myloans/myloans.component';
import { AllloansComponent } from './page/allloans/allloans.component';
import { AllemployeesComponent } from './page/allemployees/allemployees.component';
import { AllusersComponent } from './page/allusers/allusers.component';
import { AllbooksComponent } from './page/allbooks/allbooks.component';
import { PerfilComponent } from './page/perfil/perfil.component';
import { LoginadminComponent } from './page/loginadmin/loginadmin.component';
import { NavbaradminComponent } from './components/navbaradmin/navbaradmin.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AbmComponent } from './components/abm/abm.component';
import { AddbooksComponent } from './page/addbooks/addbooks.component';
import { AddloansComponent } from './page/addloans/addloans.component';
import { EditusersComponent } from './page/editusers/editusers.component';
import { EditloansComponent } from './page/editloans/editloans.component';
import { EditbooksComponent } from './page/editbooks/editbooks.component';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { Interceptor } from './services/interceptor.service';
import { EditopinionComponent } from './page/editopinion/editopinion.component';
import { AllresenalibroComponent } from './page/allresenalibro/allresenalibro.component';
@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ErrorPageComponent,

    FooterComponent,

    LoginComponent,
    SinginComponent,
    WelcomeComponent,
    ResenaComponent,
    MenuComponent,
    MyloansComponent,
    AllloansComponent,
    AllemployeesComponent,
    AllusersComponent,
    AllbooksComponent,
    PerfilComponent,
    LoginadminComponent,
    NavbaradminComponent,
    AbmComponent,
    AddbooksComponent,
    AddloansComponent,
    EditusersComponent,
    EditloansComponent,
    EditbooksComponent,
    EditopinionComponent,
    AllresenalibroComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: Interceptor,
      multi: true,
    },
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
