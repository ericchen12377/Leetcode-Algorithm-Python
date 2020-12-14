# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        return head_list == head_list[::-1]