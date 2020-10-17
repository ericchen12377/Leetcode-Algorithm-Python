# /**
#      * 迭代方法
#      * 1 -> 2 -> 3 -> 4 -> null
#      * null <- 1 <- 2 <- 3 <- 4
#      *
#      * @param head
#      * @return
#      */
#     public static ListNode reverseListIterative(ListNode head) {
#         ListNode prev = null; //前指针节点
#         ListNode curr = head; //当前指针节点
#         //每次循环，都将当前节点指向它前面的节点，然后当前节点和前节点后移
#         while (curr != null) {
#             ListNode nextTemp = curr.next; //临时节点，暂存当前节点的下一节点，用于后移
#             curr.next = prev; //将当前节点指向它前面的节点
#             prev = curr; //前指针后移
#             curr = nextTemp; //当前指针后移
#         }
#         return prev;
#     }


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        def reverse(head, tail):
            pre = tail
            while head != tail:
                t = head.next
                head.next = pre
                pre = head
                head = t
            
            return pre
        
        cur = head
        for i in range(k):
            if not cur:
                return head
            else:
                cur = cur.next
        new_head = reverse(head, cur)
        head.next = self.reverseKGroup(cur, k)
        return new_head