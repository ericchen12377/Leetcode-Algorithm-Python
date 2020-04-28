
# Definition for a Node.
# class Node(object):
#     def __init__(self, val, children):
#         self.val = val
#         self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res.append(root.val) #preorder start with root
        for child in root.children:
            res.extend(self.preorder(child)) # then child
        return res

