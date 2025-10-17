'''
枚举每根柱子的高度 h 作为矩形的高度，向左右两边找第一个高度 小于(<) h 的下标 left_i, right_i

那么此时矩形面积为 h * (right_i - left_i - 1)，求最大值即可。
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        left = [-1] * n
        right = [n] * n
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] >= h:
                right[stk[-1]] = i
                stk.pop()
            if stk:
                left[i] = stk[-1] # same as below: stk[-1] in 'i - stack[-1] - 1'
            stk.append(i)

        # valid for one element input [3]
        return max(h * (right[i] - left[i] - 1) for i, h in enumerate(heights))
