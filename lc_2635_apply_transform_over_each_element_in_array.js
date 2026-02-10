/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    return Array.from(arr, (val, i) => fn(val, i));
};
