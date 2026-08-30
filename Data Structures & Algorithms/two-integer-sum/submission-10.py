class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_nums:
                return [hash_nums.get(diff), i]
            else:
                hash_nums[nums[i]] = i