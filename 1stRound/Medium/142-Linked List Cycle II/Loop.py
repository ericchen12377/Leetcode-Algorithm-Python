# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curNode = head
        seenNodes = set()
        while curNode not in seenNodes and curNode:
            if not curNode.next:
                return None
            seenNodes.add(curNode)
            curNode = curNode.next
        return curNode