export class test {
    name: string;
    last_run: string;
    project_id: string;
    run_count: number;
    status: string;
  }
export interface testlist {
  Project: string;
  results: test[];
}
