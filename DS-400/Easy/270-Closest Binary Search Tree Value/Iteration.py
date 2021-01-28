# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        ans = root.val
        while(root):
            ans = min(root.val, ans, key=lambda x: abs(target - x))
            if target > root.val:
                root = root.right
            else:
                root = root.left
        return ans
