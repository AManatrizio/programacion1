import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResenaadminComponent } from './resenaadmin.component';

describe('ResenaadminComponent', () => {
  let component: ResenaadminComponent;
  let fixture: ComponentFixture<ResenaadminComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ResenaadminComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(ResenaadminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
