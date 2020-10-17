# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        def reverseOneGroup(pre, curnext):
            last = pre.next #last node
            cur = last.next #current ndoe
            while( cur != curnext): #not reach the node after the link
                last.next = cur.next #save 
                cur.next = pre.next
                pre.next = cur
                cur = last.next
            return last
        
        
        
        if not head or k==1:
            return head
        else:
            dummy = ListNode(-1)
            pre = dummy
            cur = head
            dummy.next = head
            
            i = 1
            while cur:
                if i % k == 0:
                    pre = reverseOneGroup(pre, cur.next)
                    cur = pre.next
                else:
                    cur = cur.next
                i = i + 1
            return dummy.next

