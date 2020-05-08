from copy import deepcopy as copy
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M or not M[0]:
            return M
        rows = len(M)
        cols = len(M[0])
        isValid = lambda i,j: i >=0 and i < rows and j >= 0 and j < cols
        row, col = 0, 0
        answer = copy(M)
        for row in range(rows):
            for col in range(cols):
                _sum, count = 0, 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if isValid(row + i, col + j):
                            _sum += M[row + i][col + j]
                            count += 1
                answer[row][col] = _sum / count
        return answer
