function updateUniqueItems(map) {
    if (!(map instanceof Map)) {
        throw new Error('Cannot process');
    }
    for (const [key, value] of map) {
        if (typeof value === 'number') {
            map.set(key, value * 2);
        }
    }
    return map;
}

export default updateUniqueItems;