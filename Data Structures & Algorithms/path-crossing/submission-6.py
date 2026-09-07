class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        seen = set()
        
        for i in path:
            seen.add((x,y))
            if i == "N":
                y += 1
            elif i == "S":
                y -= 1
            elif i == "E":
                x += 1
            else:
                x -= 1
            if (x,y) in seen:
                return True
        return False