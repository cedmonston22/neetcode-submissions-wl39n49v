class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        res = []

        for i in strs:
            anagrams["".join(sorted(i))].append(i)
        
        for value in anagrams.values():
            res.append(value)
        
        return res