class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        res = 0
        
        A = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    A[i][j] = 1 + min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1])
                    res = max(res, A[i][j])
        return res ** 2