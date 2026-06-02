class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #iterate through the array
        #store each value in another array called contains
        #check if the current value is contains if it is return true
        contains = []
        for i in nums:
            if i in contains:
                return True
            else:
                contains.append(i)
        return False