class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        diagonal_dict = defaultdict(list)
        for i in range(len(nums)):
            idx = 0
            for num in nums[i]:
                diagonal_dict[i + idx].append(num)
                idx += 1
        result = []
        for i in range(len(diagonal_dict)):
            result += diagonal_dict[i][::-1]
        return result
