# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        n = len(lists)
        
        while n > 1:
            k  = (n + 1) / 2
            for i in range(n / 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + k])
            n = k
        return lists[0]
        
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre = ListNode(-1)
        cur = pre
        
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2= l2.next
            cur = cur.next
        
        if not l1:
            cur.next = l2
        else:
            cur.next = l1
        return pre.next
    