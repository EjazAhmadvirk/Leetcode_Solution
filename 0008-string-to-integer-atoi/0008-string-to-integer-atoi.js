/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {
  s = s.trim(); // remove leading/trailing spaces
  if (s.length === 0) return 0;

  let sign = 1;
  let i = 0;
  let result = 0;
  const INT_MAX = 2 ** 31 - 1;
  const INT_MIN = -(2 ** 31);

  // check for sign
  if (s[i] === '-') {
    sign = -1;
    i++;
  } else if (s[i] === '+') {
    i++;
  }

  // process digits
  while (i < s.length && s[i] >= '0' && s[i] <= '9') {
    const digit = s.charCodeAt(i) - '0'.charCodeAt(0);

    // check for overflow
    if (result > Math.floor((INT_MAX - digit) / 10)) {
      return sign === 1 ? INT_MAX : INT_MIN;
    }

    result = result * 10 + digit;
    i++;
  }

  return result * sign;
};

// Example usage
console.log(myAtoi("42"));            // 42
console.log(myAtoi("   -42"));        // -42
console.log(myAtoi("4193 with words"));// 4193
console.log(myAtoi("words and 987")); // 0
console.log(myAtoi("-91283472332"));  // -2147483648
