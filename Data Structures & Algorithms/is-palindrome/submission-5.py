class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_chars = []

        for char in s:
            if char.isalnum():
                s_chars.append(char.lower())

        l, r = 0, len(s_chars) - 1

        while l <= r:
            if s_chars[l] != s_chars[r]:
                return False
            l += 1
            r -= 1

        return True