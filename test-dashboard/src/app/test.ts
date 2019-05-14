export class test {
    name: string;
    last_run: string;
    test_id: string;
    test_name_id: string;
    time: number;
    status: string;
    message: string;
  }
export interface testlist {
  Project: string;
  results: test[];
}
