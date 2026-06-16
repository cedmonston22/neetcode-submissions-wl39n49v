class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[]for i in range(len(nums) + 1)]
        freq = defaultdict(int)
        res =  []
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        for key, value in freq.items():
            buckets[value].append(key)
        
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res