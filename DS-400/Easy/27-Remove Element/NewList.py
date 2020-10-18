class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        res = []
        for num in nums:
            if num != val:
                res.append(num)
        nums[:] = res
        return len(nums)



nums = [3,2,2,3]
val = 3
p = Solution()
print(p.removeElement(nums,val))