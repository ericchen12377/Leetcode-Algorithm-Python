"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        curNode = head
        while curNode:
            if not curNode.child:
                curNode = curNode.next
            else:
                tail = curNode.child
                while(tail.next):
                    tail = tail.next
                tail.next = curNode.next
                if tail.next:
                    tail.next.prev = tail
                curNode.next = curNode.child
                curNode.next.prev = curNode
                curNode.child = None
        return head