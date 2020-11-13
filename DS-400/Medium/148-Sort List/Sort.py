class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        my_list, ptr = [], head
        while ptr:
            my_list.append(ptr.val)
            ptr = ptr.next
            
        my_list.sort()
        
        ptr = head
        for val in my_list:
            ptr.val = val
            ptr = ptr.next
            
        return head