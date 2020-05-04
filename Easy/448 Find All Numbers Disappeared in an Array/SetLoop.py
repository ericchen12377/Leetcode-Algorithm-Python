class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        numset = set(nums)
        N = len(nums)
        for num in range(1, N + 1):
            if num not in numset:
                res.append(num)
        return res
p = Solution()
nums = [4,3,2,7,8,2,3,1]
print(p.findDisappearedNumbers(nums))