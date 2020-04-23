class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(A)
        cols = len(A[0])
        for row in range(rows):
            A[row] = A[row][::-1] #inverse the row
            for col in range(cols):
                A[row][col] ^= 1 # invert a pixel 0 to 1, 1 to 0
        return A
input = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
p = Solution()
print(p.flipAndInvertImage(input))