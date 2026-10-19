class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[]for i in range(len(nums)+1)]
        res = []
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        for c, v in counts.items():
            buckets[v].append(c)
        

        for i in range(len(buckets)-1, 0, - 1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res
                