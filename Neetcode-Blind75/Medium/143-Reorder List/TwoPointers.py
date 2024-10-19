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
        return 
    


# https://leetcode.com/problems/reorder-list/solutions/5622171/explained-with-images-1ms-solution-beats-99/

# This Problem can be divided into three sub parts

# https://leetcode.com/problems/middle-of-the-linked-list/description/
# https://leetcode.com/problems/reverse-linked-list/description/
# Merge two lists, which we will discover in this problem.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverse(self, head):
#         if not head:
#             return None
#         prev = None
#         curr = head
#         nextNode = None
#         while curr:
#             nextNode = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nextNode
#         return prev

#     def merge(self, list1, list2):
#         while list2:
#             nextNode = list1.next
#             list1.next = list2
#             list1 = list2
#             list2 = nextNode

#     def reorderList(self, head):
#         if not head or not head.next:
#             return
#         slow = head
#         fast = head
#         prev = head
#         while fast and fast.next:
#             prev = slow
#             fast = fast.next.next
#             slow = slow.next
#         prev.next = None
#         list1 = head
#         list2 = self.reverse(slow)
#         self.merge(list1, list2)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        #find the middle node
        slow = fast = head

        while fast and fast.next:
            slow = slow.next # slow ends as the middle node, fast will go to the end
            fast = fast.next.next
        
        #reverse the second part of the list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        #merge the two sorted lists
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next