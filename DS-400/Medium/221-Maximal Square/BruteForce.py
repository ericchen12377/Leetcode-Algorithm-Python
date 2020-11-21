class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        maxRows = len(matrix)
        maxCols = len(matrix[0])
        maxLength = 0
        
        memArr = [['-1' for _ in range(maxCols)] for _ in range(maxRows)]
        
        for i in range(maxRows):
            for j in range(maxCols):
                if matrix[i][j] == '1':
                    length = self.getLength(matrix, i, j, maxRows, maxCols, memArr)
                    maxLength = max(length, maxLength)
        return maxLength**2
        
    def getLength(self, matrix, row, col, maxRows, maxCols, memArr):
        # We can get away with simple 'and' condition as the matrix is always square and never a rectangle
        if 0 <= row < maxRows and 0 <= col < maxCols:
            if memArr[row][col] != '-1':
                return memArr[row][col]
            
            if matrix[row][col] == '1':
                memArr[row][col] = 1 + min(
                                self.getLength(matrix, row+1, col, maxRows, maxCols, memArr),
                                self.getLength(matrix, row, col+1, maxRows, maxCols, memArr),
                                self.getLength(matrix, row+1, col+1, maxRows, maxCols, memArr)
                              )
            else:
                memArr[row][col] = 0
                
            return memArr[row][col]

        return 0