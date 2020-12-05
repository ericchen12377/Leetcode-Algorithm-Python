class Solution(object):
    def wallsAndGates(self, matrix):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        wall = -1
        gate = 0
        empty = 2147483647
        directions = [[-1,0],
                     [0,1],
                     [1,0],
                     [0,-1]]
        
        
        queue = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == gate:
                    queue.append([row, col])
        while queue:
            curPos = queue.pop(0)
            curRow = curPos[0]
            curCol = curPos[1]
            for i in range(len(directions)):
                curDir = directions[i]
                nextRow = curRow + curDir[0]
                nextCol = curCol + curDir[1]
                if nextRow < 0 or nextRow >= len(matrix) or nextCol < 0 or nextCol >= len(matrix[0]) or matrix[nextRow][nextCol] != empty:
                    continue
                matrix[nextRow][nextCol] = matrix[curRow][curCol] + 1
                queue.append([nextRow, nextCol])

                    
        