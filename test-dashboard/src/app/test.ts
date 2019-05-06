export class test {
    name: string;
    last_run: string;
    project_id: string;
    run_count: number;
    status: string;
  }
export class testlist {
  Project: string;
  results: test[];
  passed: number = 0;
  failed: number = 0;
  ignored: number = 0;
  new_failures: number = 0;
}
