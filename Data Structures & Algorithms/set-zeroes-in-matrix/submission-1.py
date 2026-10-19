class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #iterate through each row if there is a zero make the whole row 0s
        
        rows = [False] * len(matrix)
        cols = [False] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
        