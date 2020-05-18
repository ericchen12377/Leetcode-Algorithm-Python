# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        que = collections.deque()
        que.append(root)
        depth = 1
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if not node: continue
                if not node.left and not node.right:
                    return depth
                que.append(node.left)
                que.append(node.right)
            depth += 1
        return depth
