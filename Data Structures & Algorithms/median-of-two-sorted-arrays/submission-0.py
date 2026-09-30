class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = sorted(nums1 + nums2)
        if len(new_nums) % 2 == 1:
            return new_nums[len(new_nums)//2]
        else:
            return (new_nums[(len(new_nums) - 1)//2] + new_nums[len(new_nums)//2]) / 2