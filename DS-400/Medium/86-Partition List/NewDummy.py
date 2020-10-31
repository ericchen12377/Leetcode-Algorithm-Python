# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        if not head:
            return head
        dummy = ListNode(-1)
        newdummy = ListNode(-1)
        
        dummy.next = head
        cur = dummy
        pre = newdummy
        
        while(cur.next):
            if cur.next.val < x:
                pre.next = cur.next
                pre = pre.next
                cur.next = cur.next.next
                pre.next = None
            else:
                cur = cur.next
        pre.next = dummy.next
        return newdummy.next