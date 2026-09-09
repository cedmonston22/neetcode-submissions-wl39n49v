class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while matrix[i][-1] < target:
            i += 1
            if i == len(matrix):
                return False
        
        l, r = 0, len(matrix[i]) -1
        while l <= r:
            mid = (l+r) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False