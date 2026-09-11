class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_a = 0
        curr_a = 0

        while l < r:
            curr_a = (r-l) * min(heights[l], heights[r])
            max_a = max(max_a, curr_a)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_a