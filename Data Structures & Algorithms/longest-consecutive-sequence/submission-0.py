class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #can use set here since we want to check if numbers exist fast
        numSet = set(nums)
        longest = 0

        for i in nums:
            #if there isn't a directly preceding number it is the start of a sequence
            if(i-1) not in numSet:
                length = 0
                while(i + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest