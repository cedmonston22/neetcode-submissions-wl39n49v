class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        heights.append(0) 
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                popped = stack.pop()
                left_wall = stack[-1] if stack else -1
                width = (i - 1) - left_wall

                res = max(res, width * heights[popped])
            stack.append(i)
        return res

