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
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        k = k % n
        fast = head
        slow = head
        i = 0
        while i < k:
            if fast:
                fast = fast.next
            i += 1
        if not fast:
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        fast = slow.next
        slow.next = None