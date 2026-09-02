class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front, back = 0, len(numbers)-1
        while front < back:
            curr_sum = numbers[front] + numbers[back]
            if curr_sum - target == 0:
                return [front + 1, back + 1]
            elif curr_sum - target > 0:
                back -= 1
            else:
                front += 1
    
        
