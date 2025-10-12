class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        res = 0
        for c in s: # from left to right, '(()' => will never hit left==right
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2 * left)
            if left < right:
                left = right = 0

        left = right = 0 # dont forget to reset
        for c in reversed(s): # from right to left, '())' => will never hit left==right
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2 * left)
            if left > right: # reverse '<' to '>'
                left = right = 0

        return res
