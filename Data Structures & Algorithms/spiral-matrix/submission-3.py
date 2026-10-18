class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = set()
        res = []
        m = len(matrix)
        n = len(matrix[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        r,c = 0, 0
        d = 0
        while len(res) < n * m:
            seen.add((r,c))
            res.append(matrix[r][c])
            dr, dc = directions[d]
            nr, nc = r + dr, c + dc
            if not(0 <= nr < m and 0 <= nc < n and (nr,nc) not in seen):
                d = (d+1) % 4
                dr, dc = directions[d]
            r += dr
            c += dc
        return res
