# Problem Statement: https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''One string is a permutation of another if the two strings
       have the same character frequencies
       
       Hence:
           - find freq dict for s1
           - find freq dict for substrings of s2 (that are the same size as s1)
           
       runtime: O(n*k^2)
       '''
       
        from collections import Counter
        d1 = Counter(s1)
        k = len(s1)
        for i in range(len(s2)):  # ---- O(n)
            sub = s2[i:i+k]  # ------ O(k)
            d2 = Counter(sub) # --- O(k)
            if d1 == d2:
                return True
        return False