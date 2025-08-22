export default function appendToEachArrayValue(array, appendString) {
  let i = 0;
  for (const val of array) {
    // eslint-disable-next-line no-param-reassign
    array[i] = appendString + val;
    i += 1;
  }
  return array;
} 