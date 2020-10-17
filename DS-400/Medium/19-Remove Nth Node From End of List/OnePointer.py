# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head
        first = head
        length = 0
        while first:
            length += 1
            first = first.next
        
        length = length - n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        
        first.next = first.next.next
        return dummy.next


        return head