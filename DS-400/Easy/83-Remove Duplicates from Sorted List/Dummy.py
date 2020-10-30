# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        pre = dummy
        dummy.next = head
        
        while pre.next:
            cur = pre.next
            while(cur.next and cur.next.val == cur.val):
                cur.next = cur.next.next
            if cur != pre.next:
                pre.next = cur.next
            else:
                pre = pre.next
        return dummy.next