class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hashmap to store the groups of anagrams
        #we we will iterate through the list, sort the word
        #see if the sorted word matches any of the hashmap keys if so add as a value else create a new key
        #return the values in the form of an array
        anagrams = {}
        res = []
        for i in strs:
            anagrams.setdefault("".join(sorted(i)), []).append(i)
        for value in anagrams.values():
            res.append(value)
        
        return res