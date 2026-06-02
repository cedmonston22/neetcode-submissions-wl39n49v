class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #iterate through the array
        #store each value in a hashmap called contains
        #check if the current value is in contains if it is return true
        contains = {}
        for i in nums:
            if i in contains:
                return True
            else:
                contains[i] = 1
        return False