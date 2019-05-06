export class Project {
  id: number;
  name: string;
}
export class Project_Wrap {
  results: Project[]
  passed: number = 0;
  failed: number = 0;
  ignored: number = 0;
  new_failures: number = 0;
}
