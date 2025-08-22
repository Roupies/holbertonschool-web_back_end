export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true; // shadowed locally
    const task2 = false; // shadowed locally
    void task; // avoid unused warnings if linting
    void task2;
  }

  return [task, task2];
} 