"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        stack = []
        stack.append(root) #put root in the stack
        res = []
        while stack:
            node = stack.pop() 
            res.append(node.val) # get root val
            stack.extend(node.children[::-1]) # go through all children on left
        return res
