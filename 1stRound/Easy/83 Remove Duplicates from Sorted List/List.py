# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        deque = []
        move = head
        while move:
            while deque and deque[-1].val == move.val:
                deque.pop()
            deque.append(move)
            move = move.next
        for i in range(len(deque) - 1):
            deque[i].next = deque[i + 1]
        return deque[0]
