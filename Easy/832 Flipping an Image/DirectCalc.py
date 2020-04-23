class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        M, N = len(A), len(A[0])
        res = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                res[i][j] = 1 - A[i][N - 1 - j] #calculate the corresponding number directly
        return res
input = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
p = Solution()
print(p.flipAndInvertImage(input))