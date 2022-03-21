# Problem Statement: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2: count += 1
        return (Counter(s1) == Counter(s2)) and (count == 0 or count == 2)
    
    
# Alternate Solution
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        bad = [] # list of bad indices
        if s1 == s2 : return True
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                bad.append(i)
                
        if  not (len(bad) == 2): return False 
        
        s1 = list(s1)
        s1[bad[0]], s1[bad[1]] = s1[bad[1]], s1[bad[0]]
        res = ""
        
        for char in s1:
            res += char
        
        return (res == s2)
'''
This solution just chooses one string (the first one) and then counts how many "bad" characters exist. 
A "bad" character is a character that doesn't match it's corresponding character in the second string. 
If there are more than 2 bad indices, one swap is not enough to make them equal. 
(In fact, if there are any odd number of bad indices, no swaps can make the two strings equal). 
We only care about the case where we have 2 bad indices. We can then make an array of the characters in the string
to then swap the two bad ones, and finally re-create the string to then compare it to our goal string.
'''