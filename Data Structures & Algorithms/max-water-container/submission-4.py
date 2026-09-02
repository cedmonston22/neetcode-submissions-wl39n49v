class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        temp_a = 0
        l,r = 0, len(heights) - 1
        while l < r:
            temp_a = (r-l) * min(heights[l], heights[r])
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            max_a = max(temp_a, max_a)
        return max_a