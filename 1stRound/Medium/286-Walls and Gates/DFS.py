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
        
        def dfs(matrix, row, col, curStep):
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or curStep > matrix[row][col]:
                return
            matrix[row][col] = curStep
            for i in range(len(directions)):
                curDir = directions[i]
                dfs(matrix, row + curDir[0], col + curDir[1], curStep + 1)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == gate:
                    dfs(matrix, row, col, 0)
        