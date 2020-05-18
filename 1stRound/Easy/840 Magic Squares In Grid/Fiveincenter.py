class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        counter = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                sub_matrix = [[grid[row + i][col + j] for j in range(3)] for i in range(3)]
                if self.magic_square(sub_matrix):
                    counter += 1
        return counter

    def magic_square(self, matrix): #magic squate has 5 in center
        is_number_right = all(1 <= matrix[i][j] <= 9 for i in range(3) for j in range(3))
        is_row_right = all(sum(row) == 15 for row in matrix)
        is_col_right = all(sum(col) == 15 for col in [[matrix[i][j] for i in range(3)] for j in range(3)])
        is_diagonal_right = matrix[1][1] == 5 and matrix[0][0] + matrix[-1][-1] == 10 and matrix[0][-1] + matrix[-1][0] == 10
        is_repeat_right = len(set(matrix[i][j] for i in range(3) for j in range(3))) == 9
        return is_number_right and is_row_right and is_col_right and is_diagonal_right and is_repeat_right
