class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        counts = 0
        neighbors = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    counts += 1
                    if i < M - 1:
                        if grid[i + 1][j] == 1:
                            neighbors += 1
                    if j < N - 1:
                        if grid[i][j + 1] == 1:
                            neighbors += 1
        return 4 * counts - 2 * neighbors
grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
p = Solution()
print(p.islandPerimeter(grid))