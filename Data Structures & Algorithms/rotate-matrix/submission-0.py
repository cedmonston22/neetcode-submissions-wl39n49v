class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #(r, c) -> (c, n - r - 1)
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-1-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = temp
        
