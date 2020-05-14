# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        que = collections.deque()
        que.append(root)
        res = set()
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft() #first left is the root
                if not node:
                    continue
                if k - node.val in res:
                    return True
                res.add(node.val)
                que.append(node.left)
                que.append(node.right)
        return False
t1 = TreeNode(5)
t1.left = TreeNode(3)
t1.right = TreeNode(6)
t1.left.left = TreeNode(2)
t1.left.right = TreeNode(4)
t1.right.right = TreeNode(7)
p = Solution()
print(p.findTarget(t1,9))
print(p.findTarget(t1,28))