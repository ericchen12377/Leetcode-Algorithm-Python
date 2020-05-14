class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row in range(len(matrix) - 1):
        	for col in range(len(matrix[0]) - 1):
        		if matrix[row][col] != matrix[row+1][col+1]: #check each match
        			return False
        return True
p= Solution()

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
print(p.isToeplitzMatrix(matrix))