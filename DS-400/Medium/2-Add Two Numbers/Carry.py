# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def AddTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        answer = head
        carry = 0
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = 1 if add >= 10 else 0
            head.next = ListNode(add % 10)
            head = head.next
            l1, l2 = l1.next, l2.next
        l = l1 if l1 else l2
        while l:
            add = l.val + carry
            carry = 1 if add >= 10 else 0
            head.next = ListNode(add % 10)
            head = head.next
            l = l.next
        if carry:
            head.next = ListNode(1)
        return answer.next

#342 + 465 = 807
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

p = Solution()
print(p.AddTwoNumbers(l1, l2).val)
print(p.AddTwoNumbers(l1, l2).next.val)
print(p.AddTwoNumbers(l1, l2).next.next.val)