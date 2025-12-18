# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# same but just left/right mirror of https://leetcode.ca/2016-03-03-94-Binary-Tree-Inorder-Traversal/
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        current = root
        s = 0 # sum
        while stack or current:
            while current:
                stack.append(current)
                current = current.right

            right_or_middle = stack.pop()
            s += right_or_middle.val
            right_or_middle.val = s

            current = right_or_middle.left

        return root
