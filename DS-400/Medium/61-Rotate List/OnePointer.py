# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        n = 1
        cur = head
        while cur.next:
            n+=1
            cur = cur.next
        cur.next = head
        
        m = n - k % n
        i = 0
        while i < m:
            cur = cur.next
            i += 1
        res = cur.next
        cur.next = None
        return res
        