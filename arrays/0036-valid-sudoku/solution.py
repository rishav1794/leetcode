class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                lookup = {}
                for i in range(row, row+3):
                    for j in range(col, col+3):
                        value = board[i][j]
                        if value == '.':
                            continue
                        if value in lookup:
                            return False
                        lookup[value] = 1
        
        for row in range(0,9):
            lookup = {}
            for col in range(0,9):
                value = board[row][col]
                if value == '.':
                    continue
                if value in lookup:
                    return False
                lookup[value] = 1

        for row in range(0,9):
            lookup = {}
            for col in range(0,9):
                value = board[col][row]
                if value == '.':
                    continue
                if value in lookup:
                    return False
                lookup[value] = 1
        return True
