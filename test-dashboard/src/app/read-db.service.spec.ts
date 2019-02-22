import { TestBed } from '@angular/core/testing';

import { ReadDbService } from './read-db.service';

describe('ReadDbService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ReadDbService = TestBed.get(ReadDbService);
    expect(service).toBeTruthy();
  });
});
