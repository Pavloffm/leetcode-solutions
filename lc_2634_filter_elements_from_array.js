/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    return arr.reduce((filtered, val, i) => fn(val, i) ? [...filtered, val] : filtered, [])
};
