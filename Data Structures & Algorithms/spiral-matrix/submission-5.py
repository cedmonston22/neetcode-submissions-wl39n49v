class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0,1), (1,0),(0,-1),(-1,0)]
        seen = set()
        m = len(matrix) #rows
        n = len(matrix[0]) #columns
        d = 0
        res = []
        r,c = 0,0

        while len(res) < m*n:
            seen.add((r,c))
            res.append(matrix[r][c])
            dr, dc = directions[d]
            nr, nc = dr + r, dc + c
            if not( 0 <= nr < m and 0 <= nc < n and (nr,nc) not in seen):
                d = (d+1)%4
                dr, dc = directions[d]

            r += dr
            c += dc
        return res

