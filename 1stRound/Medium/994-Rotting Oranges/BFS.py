class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        Q = deque()
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        for i in range(len(grid)):
          for j in range(len(grid[0])):
              if grid[i][j] == 2:
                   Q.append([i,j])
              elif grid[i][j] == 1:
                   fresh += 1
        if fresh == 0: return 0
        d = 0
        neighbours = [[0,1],[1,0],[0,-1],[-1,0]]
        while Q:
          cnt = len(Q)
          for i in range(cnt):
              u,v = Q.popleft()
              for x,y in neighbours:
                  new_x = u+x
                  new_y = v+y
                  if new_x >= 0 and new_y >= 0 and new_x < n and new_y < m and grid[new_x][new_y] == 1:
                      grid[new_x][new_y] = 2
                      Q.append([new_x,new_y])
                      fresh -= 1
          d += 1
        return d-1 if fresh == 0 else -1
