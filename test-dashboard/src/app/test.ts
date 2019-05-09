export class test {
    name: string;
    last_run: string;
    test_id: string;
    test_name_id: string;
    time: number;
    status: string;
  }
export interface testlist {
  Project: number;
  results: test[];
}
