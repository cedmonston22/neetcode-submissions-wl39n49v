class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_list = []
        for i in s:
            if i.isalnum():
                s_list.append(i.lower())
        
        l,r = 0, len(s_list) - 1

        while l <= r:
            if s_list[l] != s_list[r]:
                return False
            
            l += 1
            r -= 1

        return True