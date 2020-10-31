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
        
        dummy = ListNode(-1)
        dummy.next = head
        
        pre = dummy
        cur = head
        
        while(pre.next and pre.next.val < x):
            pre = pre.next
        cur = pre
        while cur.next:
            if cur.next.val < x:
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
                pre = pre.next
            else:
                cur = cur.next
        return dummy.next