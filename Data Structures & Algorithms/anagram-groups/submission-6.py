class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        res = []

        for i in range(len(strs)):
            anagrams["".join(sorted(strs[i]))].append(strs[i])
        for value in anagrams.values():
            res.append(value)
        return res
        