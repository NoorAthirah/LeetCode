/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let xor=0
    
    for (let index=0; index <nums.length; index++)
        xor = xor ^ nums[index]
    
    return xor
    
    
};

//approach bitmap XOR and for loop
