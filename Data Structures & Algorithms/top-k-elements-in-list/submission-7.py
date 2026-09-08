class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets =[[]for i in range(len(nums) + 1)]
        freq = defaultdict(int)
        res = []

        for i in nums:
            freq[i] += 1
        
        for key, val in freq.items():
            buckets[val].append(key)

        for i in range(len(buckets) - 1, 0, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res