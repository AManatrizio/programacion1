import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditopinionComponent } from './editopinion.component';

describe('EditopinionComponent', () => {
  let component: EditopinionComponent;
  let fixture: ComponentFixture<EditopinionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EditopinionComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EditopinionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
