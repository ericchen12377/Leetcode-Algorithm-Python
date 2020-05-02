class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]: area += grid[i][j] * 4 + 2 #area for each bar
                if i: area -= min(grid[i][j], grid[i-1][j]) * 2 # minus covered area for both
                if j: area -= min(grid[i][j], grid[i][j-1]) * 2
        return area
grid = [[2,2,2],[2,1,2],[2,2,2]]
p = Solution()
print(p.surfaceArea(grid))