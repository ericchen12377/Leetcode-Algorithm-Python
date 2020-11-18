class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        
        def helper(grid, visited, x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0' or visited[x][y]:
                return None
            visited[x][y] = True
            helper(grid, visited, x - 1, y)
            helper(grid, visited, x + 1, y)
            helper(grid, visited, x, y - 1)
            helper(grid, visited, x, y + 1)
            
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        res = 0
        visited = [[None for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or visited[i][j]:
                    continue
                helper(grid, visited, i, j)
                res+=1
        return res