"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
import collections
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        depth = 0
        que = collections.deque()
        que.append(root)
        while que:
            size = len(que) #BFS
            for i in range(size):
                node = que.popleft()
                for child in node.children:
                    que.append(child)
            depth += 1 #check each level
        return depth
