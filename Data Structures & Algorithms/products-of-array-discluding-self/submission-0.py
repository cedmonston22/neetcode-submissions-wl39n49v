class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Iterate through the list to find the product of all the values excepte the value we are on
        #Avoiding divison so we have to get the products of the values before and after a certain number
        res = [1] * (len(nums))
        prefix = 1
        #Nothing comes before first value so we put 1
        for i in range(len(nums)):
            res[i] = prefix
            #Updates prefix to be the product of what comes before the next value
            prefix *= nums[i]
        postfix = 1
        #Same thing but starting from the back of the array and multiplying those values into prefixes
        for j in range(len(nums) - 1, -1, -1):
            #Nothing comes after the end of the array so postfix also starts at 1
            res[j] *= postfix
            postfix *= nums[j]
        return res

        