class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #new pos = (c, n - r - 1)
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n - i - 1):
                temp = matrix[i][j]
                a = matrix[i][j]
                b = matrix[j][n-i-1]
                c = matrix[n-i-1][n-j-1]
                d = matrix[n-j-1][i]

                matrix[i][j] = d
                matrix[n-j-1][i] = c
                matrix[n-i-1][n-j-1] = b
                matrix[j][n-i-1] = temp
