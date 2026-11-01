class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[i] < heights[stack[-1]]:
                popped = stack.pop()
                left_wall = stack[-1] if stack else -1
                width = i - left_wall - 1

                max_area =  max(max_area, (width * heights[popped]))
            stack.append(i)
        return max_area
