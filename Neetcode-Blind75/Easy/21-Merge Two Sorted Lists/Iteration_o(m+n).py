# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1) # initialize dummy
        cur = dummy # cur temp point to dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1 # dummy point to l1
                l1 = l1.next # move current l1 point to next l1
            else:
                cur.next = l2 # dummy point to l2
                l2 = l2.next # move current l2 point to next l2
            cur = cur.next # move current cur point to next cur
        
        # after while ends, either l1 or l2 will point to null
        if l1:
            cur.next = l1 # dummy point to l1
        else:
            cur.next = l2 # dummy point to l2
        return dummy.next