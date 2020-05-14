class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top, front, side = 0, 0, 0
        n = len(grid)
        for i in range(n):
            x, y = 0, 0
            for j in range(n):
                if grid[i][j] != 0:
                    top += 1  # top is the count of non-zero value
                x = max(x, grid[i][j]) # front is the max along x
                print(x)
                y = max(y, grid[j][i]) # side is the max along y
                print(y)
            front += x
            side += y
        return top + front + side

grid = [[1,2],[3,4]]
p = Solution()
print(p.projectionArea(grid))