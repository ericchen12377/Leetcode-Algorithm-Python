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
        res = [[0] * c for _ in range(r)]
        row, col = 0, 0
        for i in range(M):
            for j in range(N):
                if col == c:
                    row += 1
                    col = 0
                res[row][col] = nums[i][j]
                col += 1
        return res

nums = [[1,2],[3,4]]
r = 1
c = 4
p = Solution()
print(p.matrixReshape(nums=nums,r=r,c=c))