class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #front and back pointer
        #since it is in ascending order we can move the front pointer up or back pointer down depedning on the sum
        #iterate through the list and adjust the pointers until we find the one valid solution
        r, l = 0, len(numbers) - 1
        while r < l:
            if numbers[r] + numbers[l] == target:
                return [r + 1,l + 1]
            elif numbers[r] + numbers[l] > target:
                l -= 1
            else:
                r += 1
        
