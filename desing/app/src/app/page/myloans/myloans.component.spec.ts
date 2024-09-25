import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyloansComponent } from './myloans.component';

describe('MyloansComponent', () => {
  let component: MyloansComponent;
  let fixture: ComponentFixture<MyloansComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MyloansComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MyloansComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
