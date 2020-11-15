# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        def getlength(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count
        lenA = getlength(headA)
        lenB = getlength(headB)
        
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        else:
            for i in range(lenB - lenA):
                headB = headB.next
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        if headA and headB:
            return headA
        else:
            return None