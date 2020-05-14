#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = self.inOrder(root)
        if not res:
            return 
        dummy = TreeNode(-1)
        cur = dummy
        for node in res:
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return dummy.right
    
    def inOrder(self, root):
        if not root:
            return []
        res = []
        res.extend(self.inOrder(root.left))
        res.append(root)
        res.extend(self.inOrder(root.right))
        return res


x = [5,3,6,2,4,None,8,1,None,None,None,7,9]
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)
p = Solution()
print(p.inOrder(root))
newroot = p.increasingBST(root)
print(newroot)
print(newroot.val)
#print(newroot.left)
print(newroot.right.val)
#print(newroot.left.left)
#print(newroot.left.right)
#print(newroot.right.left)
print(newroot.right.right.val)
#print(newroot.right.right.left)
print(newroot.right.right.right.val)
#print(newroot.right.right.right.left)
print(newroot.right.right.right.right.val)
print(newroot.right.right.right.right.right.val)