# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
        return [[root.val]+i for i in tmp]