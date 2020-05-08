import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == len(set(nums)):
            return 1
        counter = collections.Counter(nums)
        degree_num = counter.most_common(1)[0]
        most_numbers = [num for num in counter if counter[num] == degree_num[1]] # find the degree numbers
        scale = 100000000
        for most_number in most_numbers: #check the longest scale from the numbers
            appear = [i for i,num in enumerate(nums) if num == most_number]
            appear_scale = max(appear) - min(appear) + 1
            if appear_scale < scale:
                scale = appear_scale
        return scale
nums = [1,2,2,3,1,4,2]
p = Solution()
print(p.findShortestSubArray(nums))