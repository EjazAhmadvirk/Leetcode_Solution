# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p or not q:
      return p == q # covers: p=none and q!=none, q=none and p!=none, both none
    return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# iteration
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None:
            return q is None

        if q is None:
            return p is None

        stack1 = [p]
        stack2 = [q]

        while stack1 and stack2:
            current1 = stack1.pop()
            current2 = stack2.pop()

            if current1 is None and current2 is None:
                continue
            elif current1 is None or current2 is None:
                return False
            elif current1.val != current2.val:
                return False

            stack1.append(current1.left)
            stack2.append(current2.left)

            stack1.append(current1.right)
            stack2.append(current2.right)

        return not stack1 and not stack2
