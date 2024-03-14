/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    let pointer = 0
    for (let index=0; index < haystack.length; index++){
        if (haystack[index] !== needle[pointer]){
            index = index - pointer
            pointer =0
        }
    else if (pointer == needle.length -1) 
        return index-pointer
    else pointer++
}
    return -1
};