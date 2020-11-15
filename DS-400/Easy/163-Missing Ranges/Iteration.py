class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        nums = [lower - 1] + nums + [upper + 1]
        nums = nums[::-1]
        while nums:
            x = nums.pop()
            if x > lower + 2:
                res.append(str(lower + 1) + '->'+ str(x - 1))
            elif x == lower + 2:
                res.append(str(lower + 1))
            lower = x
                
        return  res