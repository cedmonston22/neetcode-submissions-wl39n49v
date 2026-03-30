class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Given a list of ints and a target
        #return indicies of the nums in the list that add to target
        #check the sums of all the potential pairs to see if it adds to target
        #if it adds up return the indecies
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
            
