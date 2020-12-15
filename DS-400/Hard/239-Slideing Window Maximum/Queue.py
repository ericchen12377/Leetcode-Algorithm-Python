def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    ln = len(nums)
    if ln == 0:
        return []
    
    queue = []
    for i in range(k):
        while queue and queue[-1][0] <= nums[i]:
            queue.pop()
        queue.append((nums[i], i))
    
    i = k
    result = [queue[0][0]]
    while i < ln:
        #remove the first element from the queue if it is outside the window
        if i - queue[0][1] >= k:
            queue.pop(0)
        
        # also remove any elements that are less than the current num
        # as long as the current num is in the boundary I don't care about any other number
        # if this is the max, then be it.
        while queue and queue[-1][0] <= nums[i]:
            queue.pop()
        queue.append((nums[i], i))
        
        result.append(queue[0][0])
        i += 1
    
    return result