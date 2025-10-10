class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # remove leading whitespaces
        if not s:
            return 0

        sign = 1
        i = 0
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Check for sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        # Convert digits to integer
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            # Handle overflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
