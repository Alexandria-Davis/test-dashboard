import { TestBed } from '@angular/core/testing';

import { ReadXmlService } from './read-xml.service';

describe('ReadXmlService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ReadXmlService = TestBed.get(ReadXmlService);
    expect(service).toBeTruthy();
  });
});
