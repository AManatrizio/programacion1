import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NavbarBackHomeAdminComponent } from './navbar-back-home-admin.component';

describe('NavbarBackHomeAdminComponent', () => {
  let component: NavbarBackHomeAdminComponent;
  let fixture: ComponentFixture<NavbarBackHomeAdminComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [NavbarBackHomeAdminComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NavbarBackHomeAdminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
