class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(matrix[row+1][1:] == matrix[row][:-1] for row in range(len(matrix)-1)) #slice match one in a row and forward one in second row
p= Solution()

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
print(p.isToeplitzMatrix(matrix))