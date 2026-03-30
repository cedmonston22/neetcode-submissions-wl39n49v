class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char
        front = 0
        back = len(new_s) - 1
        while front < back:
            if new_s[front].lower() != new_s[back].lower():
                return False
            else:
                front += 1
                back -= 1
        return True