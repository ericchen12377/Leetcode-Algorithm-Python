class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k %= N
        self.reverse(nums, 0, N - 1);
        self.reverse(nums, 0, k - 1);
        self.reverse(nums, k, N - 1);

    def reverse(self, nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
