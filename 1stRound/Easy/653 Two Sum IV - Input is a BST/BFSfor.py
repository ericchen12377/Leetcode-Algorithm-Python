# Definition for a binary tree node.
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
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            print(i.val)
            if k - i.val in s: 
                return True
            s.add(i.val)
            if i.left : bfs.append(i.left)
            if i.right : bfs.append(i.right)
            print([b.val for b in bfs])
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