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
        if not head:
            return None
        slow = head
        fast = head
        
        while True:
            fast = fast.next
            slow = slow.next
            if not fast or not fast.next:
                return None
            else:
                fast = fast.next
            if slow == fast:
                break
        p1 = head
        p2 = slow
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1