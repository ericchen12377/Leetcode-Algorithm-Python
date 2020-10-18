class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if(len(nums)==0):
            return 0
        else:
            slow = 0
            fast = 1
            while(fast < len(nums)):
                if(nums[fast]!=nums[slow]):
                    slow += 1
                    nums[slow] = nums[fast]
                fast += 1
            return slow + 1
                    


nums = [1,1,2]
p = Solution()
print(p.removeDuplicates(nums))