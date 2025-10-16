# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        current = root
        res = []
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            left_or_middle = stack.pop()
            res.append(left_or_middle.val)
            current = left_or_middle.right
        return res