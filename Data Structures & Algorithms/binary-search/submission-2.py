class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            for i in range(0, mid):
                if nums[i] == target:
                    return i
        elif nums[mid] < target:
            for j in range(mid + 1, len(nums)):
                if nums[j] == target:
                    return j
        return -1