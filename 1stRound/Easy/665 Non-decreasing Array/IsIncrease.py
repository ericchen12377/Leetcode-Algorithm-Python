class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        isIncrease = lambda nums: all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
        one, two = nums[:], nums[:]
        for i in range(0, len(nums) - 1):
            if nums[i + 1] < nums[i]:
                one[i] = one[i + 1]
                two[i + 1] = two[i]
                break
        return isIncrease(one) or isIncrease(two)
