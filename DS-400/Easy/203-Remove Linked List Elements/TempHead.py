# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        res = None
        while head:
            if not res and head.val != val:             # Set the head node whose value is not == val
                res = head
            if head.next and head.next.val == val:      # Remove the nodes whose value == val
                head.next = head.next.next
            else:                                       # Skip the nodes with different val
                head = head.next
        return res


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if not head:
            return head
        while head and head.val == val:
            head = head.next
        temp = head
        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp =  temp.next
        return head