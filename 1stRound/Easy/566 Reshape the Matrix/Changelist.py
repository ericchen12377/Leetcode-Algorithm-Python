class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        M, N = len(nums), len(nums[0])
        if M * N != r * c:
            return nums
        res = []
        row = []
        for i in range(M):
            for j in range(N):
                row.append(nums[i][j])
                if len(row) == c:
                    res.append(row)
                    row = []
        return res

nums = [[1,2],[3,4]]
r = 1
c = 4
p = Solution()
print(p.matrixReshape(nums=nums,r=r,c=c))