class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * (n)
        fwd = [1] * (n)
        bwd = [1] * (n)
        fwd[0] = 1
        bwd[n-1] = 1
        
        for i in range(1,n):
            fwd[i] = fwd[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            bwd[i] = bwd[i+1] * nums[i+1]
        for i in range(n):
            res[i] = fwd[i] * bwd[i]
        return res