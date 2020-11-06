# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
          return True

        stack = [[root.left, root.right]]

        while stack:
          left, right = stack.pop()

          if left is None and right is None:
            continue
          if left is None or right is None:
            return False
          if left.val == right.val:
            stack.insert(0, [left.left, right.right])

            stack.insert(0, [left.right, right.left])
          else:
            return False
        return True