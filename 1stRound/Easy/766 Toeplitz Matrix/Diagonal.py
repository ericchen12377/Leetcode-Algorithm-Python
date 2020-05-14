class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0])
        for row in range(M):
            first = matrix[row][0]
            j = 0
            for i in range(row, M):
                if 0 <= j < N:
                    if matrix[i][j] != first:
                        return False
                j += 1
        for col in range(N):
            first = matrix[0][col]
            i = 0
            for j in range(col, N):
                if 0 <= i < M:
                    if matrix[i][j] != first:
                        return False
                i += 1
        return True
p= Solution()

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
print(p.isToeplitzMatrix(matrix))