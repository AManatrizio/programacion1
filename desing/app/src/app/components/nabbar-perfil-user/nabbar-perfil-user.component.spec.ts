import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NabbarPerfilUserComponent } from './nabbar-perfil-user.component';

describe('NabbarPerfilUserComponent', () => {
  let component: NabbarPerfilUserComponent;
  let fixture: ComponentFixture<NabbarPerfilUserComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [NabbarPerfilUserComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NabbarPerfilUserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
