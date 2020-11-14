# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        if not root: return None
        stack = []
        p = root
        while p:
            stack.append(p)
            #print (p.val)
            p = p.left
        ans = stack.pop()
        prev = ans
        while stack:
            curr = stack.pop()
            prev.left = curr.right
            curr.left = None
            curr.right = None
            prev.right = curr
            #print(curr.val)
            prev =  curr
        #print(ans)
        return ans
        