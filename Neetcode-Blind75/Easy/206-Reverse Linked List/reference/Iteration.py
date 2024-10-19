# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        pre = None #last node
        cur = head #current ndoe
        while( cur != None): #not reach the node after the link
            nextTemp = cur.next #save 
            cur.next = pre
            pre = cur
            cur = nextTemp
        return pre