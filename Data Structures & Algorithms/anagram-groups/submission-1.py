from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #check if words are anagrams
        #have to iterate through the whole list
        anagrams = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            anagrams[sortedS].append(s)
        return list(anagrams.values())