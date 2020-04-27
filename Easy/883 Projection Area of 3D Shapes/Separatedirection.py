class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        rowMax, colMax = [0] * M, [0] * N
        xy = sum(0 if grid[i][j] == 0 else 1 for i in range(M) for j in range(N))
        xz = sum(list(map(max, grid)))
        yz = sum(list(map(max, [[grid[i][j] for i in range(M)] for j in range(N)])))
        return xy + xz + yz
grid = [[1,2],[3,4]]
p = Solution()
print(p.projectionArea(grid))