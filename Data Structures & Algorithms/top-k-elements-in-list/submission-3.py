class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Put every element from nums into a hashmap
        #Since they can be in any order,
        #directly iterate through hashmap to find k amount of largest values
        #Once you have checked the whole hashmap return the keys
        freq = {}
        count_bucket = [[]for i in range(len(nums)+1)]
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        for key, v in freq.items():
            count_bucket[v].append(key)
        
        res = []
        for j in range(len(count_bucket)-1, 0, -1):
            for v in count_bucket[j]:
                if v == None:
                    continue
                res.append(v)
                if len(res) == k:
                    return res