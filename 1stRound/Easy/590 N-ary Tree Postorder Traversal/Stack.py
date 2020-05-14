"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []  #post order is left right root
        if not root:
            return res
        stack = [root,] # use stack with root, right and left, and reverse the result
        while stack:
            node = stack.pop()
            stack.extend(node.children)
            res.append(node.val)
        return res[::-1] #reverse the result
