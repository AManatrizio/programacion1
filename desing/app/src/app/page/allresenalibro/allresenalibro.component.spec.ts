import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AllresenalibroComponent } from './allresenalibro.component';

describe('AllresenalibroComponent', () => {
  let component: AllresenalibroComponent;
  let fixture: ComponentFixture<AllresenalibroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AllresenalibroComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AllresenalibroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
