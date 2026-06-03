class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Get the string into only alphanumerical characters
        #Have a pointer starting at the front and one on the back and check if they are equal
        #Keep checking until the pointers are equal or the front pointer is greater than the back pointer
        string = ""
        for i in s:
            if i.isalnum():
                string += i.lower()
        p1 = 0
        p2 = len(string) - 1
        while p1 < p2:
            if string[p1] != string[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True