/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  let res = 0;
  for (let i = 0; i < 32; i++) {
    const bit = (n >> i) & 1;
    res |= bit << (31 - i);
  }
  return res >>> 0;
 // unsigned right shift ( >>> ) operator returns a number whose binary representation is the first operand shifted by the specified number of bits to the right.
    
    //(>>) operator returns a number or BigInt whose binary representation is the first operand shifted by the specified number of bits to the right
    // (|=) operator performs bitwise OR on the two operands and assigns the result to the left operand.
};