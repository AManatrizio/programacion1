import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddloansComponent } from './addloans.component';

describe('AddloansComponent', () => {
  let component: AddloansComponent;
  let fixture: ComponentFixture<AddloansComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AddloansComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddloansComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
