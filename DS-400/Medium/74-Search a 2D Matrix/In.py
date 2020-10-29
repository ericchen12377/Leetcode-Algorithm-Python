class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        size = len(matrix)
        for i in range(size):
            if target in matrix[i]:
                return True
        return False