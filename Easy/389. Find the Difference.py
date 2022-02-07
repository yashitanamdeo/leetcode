# Problem Statement: https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for letter in t:
            if t.count(letter) != s.count(letter):
                return letter

# Alternate Solution 1
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

#Alternate Solution 2
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counts = Counter(s)
        t_counts = Counter(t)
        for i in t_counts:
            if t_counts[i] > s_counts[i]:
                return i  
            
        