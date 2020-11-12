# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        if not head or not head.next or not head.next.next:
            return 
        fast = head
        slow = head
        #find the middle point
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        
        #flip the second list after mid
        slow.next = None
        last = mid
        pre = None
        while last:
            nxt = last.next
            last.next = pre
            pre = last
            last = nxt
        
        #insert second list to first list
        while head and pre:
            nxt = head.next
            head.next = pre
            pre = pre.next
            head.next.next = nxt
            head = nxt
        return head