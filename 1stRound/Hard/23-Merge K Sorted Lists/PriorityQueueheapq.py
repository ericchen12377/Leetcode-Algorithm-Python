# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return None
        start = ListNode() # Dummy node
        cur = start
        hq = []
        # Push first node of each list into heapq
        for i, it in enumerate(lists):
            if it: heapq.heappush(hq, (it.val, i))
        while hq:
            _, i = heapq.heappop(hq) # Pop minimum value in heapq and its corresponding index
            cur.next = lists[i]
            cur = cur.next
            lists[i] = lists[i].next
            if lists[i]: heapq.heappush(hq, (lists[i].val, i)) # Do not push None into heapq
        return start.next