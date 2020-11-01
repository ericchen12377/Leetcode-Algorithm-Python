# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        pre = None #last node
        cur = head #current ndoe

        while(m > 1): #not reach the node after the link
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1
        
        tail, con = cur, pre
        
        while n:
            nextTemp = cur.next #save 
            cur.next = pre
            pre = cur
            cur = nextTemp
            n -= 1
        
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = cur
        return head
        