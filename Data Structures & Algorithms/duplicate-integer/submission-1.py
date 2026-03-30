class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #given array of ints
        #return a bool to see if there are duplicate numbers
        #Iterate through the original list
        #Compare the value to see if it is another array 'check' if it is return true else append the value to the array
        check : [int] = []
        for i in range(len(nums)):
            if nums[i] in check:
                return True
            else:
                check.append(nums[i])
        return False