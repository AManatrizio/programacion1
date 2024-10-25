import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditloansComponent } from './editloans.component';

describe('EditloansComponent', () => {
  let component: EditloansComponent;
  let fixture: ComponentFixture<EditloansComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EditloansComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EditloansComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
