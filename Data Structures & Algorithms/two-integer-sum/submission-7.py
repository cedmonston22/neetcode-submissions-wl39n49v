class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #iterate through nums for each item in nums
        #create another loop inside to check each possible sum
        #if the sum equals the target return the indices from each loop
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]