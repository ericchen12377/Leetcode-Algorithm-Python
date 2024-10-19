# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        first = head # start with first, save first
        tail = head # save head as tail
        second = first.next # start second
        while second:
            tmp = second.next # save third before changing second
            second.next = first # reverse pointer of second to first
            first = second # move first pointer to second
            second = tmp # move second pointer to tmp, which is third
        print
        head.next = None # after while, reverse head.next to null
        head = first # 

        return head
        