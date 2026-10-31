class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0 , len(height) - 1

        leftMax = height[l]
        rightMax = height[r]
        totalWater = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                totalWater += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                totalWater += rightMax - height[r]
        return totalWater
