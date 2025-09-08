function createInt8TypedArray(length, position, value) {
    if (position < 0 || position >= length) {
        throw new Error('Position out of range');
    }
    const int8Array = new Int8Array(length);
    int8Array[position] = value;
    return int8Array;
}

export default createInt8TypedArray; 