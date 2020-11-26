class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ct_0, ct_1, ct_2 = 0, 0, 0
        for i in nums:
            if i == 0:
                ct_0 += 1
            elif i == 1:
                ct_1 += 1
            elif i == 2:
                ct_2 += 1
        nums[:] = [0]*ct_0 + [1] * ct_1 + [2] * ct_2