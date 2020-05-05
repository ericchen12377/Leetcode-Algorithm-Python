class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = cm = 0
        for num in nums:
            if m == num:
                cm += 1
            elif cm == 0:
                m = num
                cm = 1
            else:
                cm -= 1
        return m
