class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        slow = 0
        fast = 0
        while(fast < len(nums)):
            if(nums[fast]!= val):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow,nums



nums = [3,2,2,3]
val = 3
p = Solution()
print(p.removeElement(nums,val))