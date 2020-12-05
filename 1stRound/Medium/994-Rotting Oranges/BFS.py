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



class Solution(object):
    def orangesRotting(self, matrix):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Sequential order
        #-Count fresh oranges
        #-put rotten oranges into queue
        
        #BFS:
        #-use queue size to track minutes
        #-process rotting oranges
          #-rot adjacent fresh oranges
          #-push into queue
          #-decrement fresh oranges count
            
        directions = [[-1,0],
                     [0,1],
                     [1,0],
                     [0,-1]]
        rotten = 2
        fresh = 1
        empty = 0
        
        if len(matrix) == 0:
            return 0
        queue = []
        freshoranges = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == rotten:
                    queue.append([row,col])
                if matrix[row][col] == fresh:
                    freshoranges += 1
        curQueueSize = len(queue)
        minutes = 0
        while len(queue) > 0:
            if curQueueSize == 0:
                minutes += 1
                curQueueSize = len(queue)
            curOrange = queue.pop(0)
            curQueueSize -= 1
            row = curOrange[0]
            col = curOrange[1]
            
            for i in range(len(directions)):
                curDir = directions[i]
                nextRow = curDir[0] + row
                nextCol = curDir[1] + col
                if nextRow < 0 or nextRow >= len(matrix) or nextCol < 0 or nextCol >= len(matrix[0]):
                    continue
                if matrix[nextRow][nextCol] == fresh:
                    matrix[nextRow][nextCol] = 2
                    freshoranges -= 1
                    queue.append([nextRow, nextCol])
        if freshoranges > 0:
            return -1
        return minutes
            
                    
        
