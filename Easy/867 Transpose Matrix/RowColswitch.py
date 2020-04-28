class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(A), len(A[0])
        res = [[0] * rows for _ in range(cols)] # new empty matrix
        for row in range(rows):
            for col in range(cols):
                res[col][row] = A[row][col] #put in numbers
        return res

A = [[1,2,3],[4,5,6],[7,8,9]]
p = Solution()
print(p.transpose(A))