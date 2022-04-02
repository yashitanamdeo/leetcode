# Problem Statement: https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                delete_i = s[i+1:j+1]
                delete_j = s[i:j]
                return self._isPalindrome(delete_i) or self._isPalindrome(delete_j)
            i += 1
            j -= 1
        return True
    
    def _isPalindrome(self, s):
        return s == s[::-1]