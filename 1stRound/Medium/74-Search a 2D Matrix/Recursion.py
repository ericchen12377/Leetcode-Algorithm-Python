class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        elif not matrix[0]:
            return False
        elif target <= matrix[0][-1]:
            return target in matrix[0]
        elif target > matrix[0][-1]:
            matrix.pop(0)
            return self.searchMatrix(matrix, target)