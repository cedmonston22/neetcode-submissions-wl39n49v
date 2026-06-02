class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Since order doesn't matter, we put all the characters of each string into a hashmap
        #Compare if the values of each key in the hashmap are equal
        if(len(s) != len(t)):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True