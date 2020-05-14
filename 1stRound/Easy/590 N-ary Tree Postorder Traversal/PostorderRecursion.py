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
        res = []
        if not root:
            return res
        for child in root.children:
            res.extend(self.postorder(child))  #post-order start with left, then right 
        res.append(root.val) # then root
        return res
