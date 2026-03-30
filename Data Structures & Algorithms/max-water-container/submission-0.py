class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                if heights[i] < heights[j]:
                    temp = heights[i] * (j - i)
                else:
                    temp = heights[j] * (j- i)
                if temp > max:
                    max = temp
        return max