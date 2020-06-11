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
        if not l1:
            return l2
        if not l2:
            return l1
        add = l1.val + l2.val
        res = ListNode(add % 10)
        res.next = self.AddTwoNumbers(l1.next, l2.next)
        if add >= 10:
            res.next = self.AddTwoNumbers(res.next, ListNode(1))
        return res

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
