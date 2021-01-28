class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []

        col_begin = 0
        col_end = len(matrix)

        row_begin = 0
        row_end = len(matrix[0])

        matrix_size = len(matrix) * len(matrix[0])

        while True:

            if len(answer) < matrix_size:
                # right
                for i in range(row_begin, row_end):
                    answer.append(matrix[row_begin][i])
                col_begin += 1

            if len(answer) < matrix_size:
                # down
                for i in range(col_begin, col_end):
                    answer.append(matrix[i][row_end-1])
                row_end -= 1

            if len(answer) < matrix_size:
                # left
                for i in range(row_end-1, row_begin-1, -1):
                    answer.append(matrix[col_end-1][i])
                col_end -= 1

            if len(answer) < matrix_size:
                # up
                for i in range(col_end-1, col_begin-1, -1):
                    answer.append(matrix[i][row_begin])
                row_begin += 1

            if not len(answer) < matrix_size:
                break

        return answer
