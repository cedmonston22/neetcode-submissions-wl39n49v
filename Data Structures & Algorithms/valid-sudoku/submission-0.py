class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #We are going to check each row individually to see that there are no duplicates
        #Then check the column to see that there are no duplicates
        #Then Check the 3x3 grid to make sure there are no duplicates
        #We can create a hashmap for each the row, col, and our 3x3 grid
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) #keys are (rows//3, cols//3) so then it is 0-2

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i] or
                    board[i][j] in cols[j] or
                    board[i][j] in squares[(i//3, j//3)]):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3, j//3)].add(board[i][j])
        return True
                