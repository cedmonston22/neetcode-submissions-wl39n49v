class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #have two pointers that check the values after our start value and at the end of the array
        #sort the array so we can adjust pointers to reach 0
        #If our current starting value is the same as the previous starting skip
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
