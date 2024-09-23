import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NavbarBackHomeComponent } from './navbar-back-home.component';

describe('NavbarBackHomeComponent', () => {
  let component: NavbarBackHomeComponent;
  let fixture: ComponentFixture<NavbarBackHomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [NavbarBackHomeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NavbarBackHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
