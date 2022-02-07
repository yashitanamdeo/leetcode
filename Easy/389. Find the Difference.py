# Problem Statement: https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for letter in t:
            if t.count(letter) != s.count(letter):
                return letter

# Alternate Solution
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        
        s = sorted(s)
        t = sorted(t)
        
        for index, s_val in enumerate(s):
            if t[index] != s_val:
                return t[index]
        
        return t[-1]