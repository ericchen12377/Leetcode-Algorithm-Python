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
        def reverse(prev, current, m):
            nxt = current.next
            current.next = prev
            if m == 0:
                return current, nxt
            return reverse(current, nxt, m - 1)

        lth = None
        mth = head

        for i in range(1, m):
            lth = mth
            mth = mth.next

        nth, oth = reverse(lth, mth, n - m)
        if lth:
            lth.next = nth
        else:
            head = nth
        mth.next = oth
        return head
            