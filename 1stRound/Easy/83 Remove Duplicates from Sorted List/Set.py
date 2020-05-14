# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        val_set = set()
        val_set.add(head.val)
        root = ListNode(0)
        root.next = head
        while head and head.next:
            if head.next.val in val_set:
                head.next = head.next.next
            else:
                head = head.next
                val_set.add(head.val)
        return root.next
