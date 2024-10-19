# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return
        stack=[]
        node=head
        # store the list into stack
        while node:
            stack.append(node)
            node=node.next

        node=head #node is the forward list, stack will be poped in backwards
        #use half of the list and stack
        for i in range(len(stack)//2):
            print('loop i',i)
            n=stack.pop() #pop the last of stack first, save it
            print(n.val)
            t=node.next # save the next node in the list
            print(t.val)
            node.next=n # point the next node to last stack
            print(node.next.val)
            n.next=t # point the next of last stack to the next in the list
            print(n.next.val)
            node=t # point back to the next node in the list, to go forward
            print(node.val)
            print(node.next.val)
        print(node.next.val)    
        node.next=None # node is already in the middle, naturally become the tail of the list, point to null
        print(head.val)    
        print(head.next.val)    
        print(head.next.next.val)    
        print(head.next.next.next.val)    
        print(node.val)    
        # print(node.next.val)    
        # # Method 1: Using a stack
        # if head.next is None or head.next.next is None:
        #     return
        # st = []
        # t = head
        # while t:
        #     st.append(t)
        #     t = t.next
        # s = head
        # s_n = head.next
        # while len(st)!=0 and s_n:
        #     st.pop(0)
        #     t = st.pop()
        #     s.next = t
        #     if len(st)==0:
        #         t.next = None
        #     else:
        #         t.next = s_n
        #     if len(st)!=0:
        #         st[-1].next = None
        #     else:
        #         break
        #     s = s_n
        #     s_n = s_n.next