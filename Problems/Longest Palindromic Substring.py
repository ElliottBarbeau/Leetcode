#Brute force with bad space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s
        longest = 0
        substr = ""
        for i, char in enumerate(s):
            for j, char2 in enumerate(s):
                if j - i >= longest and self.isPalindrome(s[i:j+1]):
                    longest = j - i
                    substr = s[i:j+1]
        return substr


    def reverse(self, s): 
        return s[::-1] 

    def isPalindrome(self, s): 
        # Calling reverse function 
        rev = self.reverse(s) 

        # Checking if both string are equal or not 
        if (s == rev): 
            return True
        return False