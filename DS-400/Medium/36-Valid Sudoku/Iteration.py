class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.' and not self.isValidCell(row, col, board):
                    return False
        return True
    def isValidCell(self, row: int, col: int, board: List[List[str]]) -> bool:
        return self.isValidRow(row, board) and self.isValidCol(col, board) and self.isValidBox(row, col, board)
    def isValidRow(self, row: int, board: List[List[str]]) -> bool:
        d = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        for cell in board[row]:
            if cell != '.':
                d[cell] += 1
                if d[cell] > 1:
                    return False
        return True
    def isValidCol(self, col: int, board: List[List[str]]) -> bool:
        d = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        for row in range(9):
            cell = board[row][col]
            if cell != '.':
                d[cell] += 1
                if d[cell] > 1:
                    return False
        return True
            
    def isValidBox(self, row: int, col: int, board: List[List[str]]) -> bool:
        d = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for row in range(start_row, start_row+3):
            for col in range(start_col, start_col+3):
                cell = board[row][col]
                if cell != '.':
                    d[cell] += 1
                    if d[cell] > 1:
                        return False
        return True