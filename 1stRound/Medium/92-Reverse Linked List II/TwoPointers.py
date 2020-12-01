# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        curpos = 1
        curNode = head
        start = head
        
        while curpos < m:
            start = curNode
            curNode = curNode.next
            curpos += 1
        
        newlist = None
        tail = curNode
        while curpos >= m and curpos <= n:
            nextTemp = curNode.next
            curNode.next = newlist
            newlist = curNode
            curNode = nextTemp
            curpos += 1
        start.next = newlist
        tail.next = curNode
        if m > 1:
            return head
        else:
            return newlist
            