class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        
        directions = [[-1,0],
                     [0,1],
                     [1,0],
                     [0,-1]]
        if not grid:
            return 0
        islandCount = 0
        queue = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islandCount += 1
                    print(islandCount)
                    queue.append([row, col])
                    while queue:
                        currentPos = queue.pop(0)
                        curRow = currentPos[0]
                        curCol = currentPos[1]
                        grid[curRow][curCol] = 0
                        for i in range(len(directions)):
                            curDir = directions[i]
                            nextRow = curRow + curDir[0]
                            nextCol = curCol + curDir[1]
                            if nextRow < 0 or nextRow >= len(grid) or nextCol < 0 or nextCol >= len(grid[0]):
                                continue
                            if grid[nextRow][nextCol] == "1":
                                queue.append([nextRow, nextCol])
        return islandCount