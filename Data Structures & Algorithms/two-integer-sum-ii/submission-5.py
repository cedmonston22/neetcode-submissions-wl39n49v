class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = defaultdict(int)
        for i in range(len(numbers)):
            if target - numbers[i] in num_map:
                return[num_map[target - numbers[i]] + 1, i + 1]
            else:
                num_map[numbers[i]] = i
