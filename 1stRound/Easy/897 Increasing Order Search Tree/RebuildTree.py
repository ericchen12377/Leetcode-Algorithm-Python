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
        array = self.inOrder(root)
        if not array:
            return None
        newRoot = TreeNode(array[0])
        curr = newRoot
        for i in range(1, len(array)):
            curr.right =TreeNode(array[i])
            curr = curr.right
        return newRoot
        
    def inOrder(self, root):
        if not root:
            return []
        array = []
        print(array)
        array.extend(self.inOrder(root.left))
        print(array)
        array.append(root.val)
        print(array)
        array.extend(self.inOrder(root.right))
        print(array)
        return array

x = [5,3,6,2,4,None,8,1,None,None,None,7,9]
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(4)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
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