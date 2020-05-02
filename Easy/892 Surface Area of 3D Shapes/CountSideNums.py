class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        inner = 0
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                count += grid[i][j]
                if i < M - 1 and grid[i + 1][j] != 0:
                    inner += min(grid[i][j], grid[i + 1][j])
                if j < N - 1 and grid[i][j + 1] != 0:
                    inner += min(grid[i][j], grid[i][j + 1])
                if grid[i][j] >= 2:
                    inner += grid[i][j] - 1
        print(count, inner)
        return count * 6 - inner * 2
grid = [[2,2,2],[2,1,2],[2,2,2]]
p = Solution()
print(p.surfaceArea(grid))