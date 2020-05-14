# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        que = collections.deque()
        res = []
        que.append(root)
        while que:
            size = len(que)
            row = []
            for _ in range(size):
                node = que.popleft()
                if not node:
                    continue
                row.append(node.val)
                que.append(node.left)
                que.append(node.right)
            if row:
                res.append(sum(row) / float(len(row)))
        return res
