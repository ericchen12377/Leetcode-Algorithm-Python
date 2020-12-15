from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue, res = deque(), []
        for i in range(len(nums)):
            # Need to drop the element which is not in the window of size k
            if queue and i-queue[0]==k: queue.popleft()
            # Need to insert the curr index. And remove all the elements smaller than element at curr index
            while queue and nums[queue[-1]]<=nums[i]: queue.pop()
            queue.append(i)
            # If our current window is equal to or bigger than k, only then append in result
            if i+1>=k: res.append(nums[queue[0]])   
        return res