class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)):
            if sorted(s2[i:len(s1) + i]) == sorted(s1):
                return True

        return False