"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def copyNode(blue, cache):
            if not blue:
                return None
            if blue in cache:
                return cache[blue]
            copy = Node(blue.val)
            cache[blue] = copy
            copy.next = copyNode(blue.next, cache)
            copy.random = copyNode(blue.random, cache)
            return copy
        return copyNode(head, {})