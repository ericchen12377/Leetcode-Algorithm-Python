# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        N = len(vals)
        left, right = 0, N - 1
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1
        return True
