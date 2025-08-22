export function taskFirst() {
  const message = 'I prefer const when I can.';
  return message;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  let phrase = 'But sometimes let';
  phrase += getLast();
  return phrase;
} 