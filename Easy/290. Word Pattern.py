# Problem Statement: https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {} # word - key, and letter - value
        d2 = {} # to keep track of all the letters we are going to use
        
        words = s.split()
        # base case
        if len(words) != len(pattern): return False # no. of words should be equal to no. of characters in the string pattern
        
        i = 0
        while i < len(words):
            if words[i] not in d and pattern[i] not in d2: # if words[i] is not in hashmap/dictionary
                d[words[i]] = pattern[i] # add in hashmap/dictionary
                d2[pattern[i]] = True
            elif d.get(words[i]) != pattern[i]: return False # if it doesn't exists then get method will return None. This is to remove key value error
            i += 1
        return True

# Post: https://leetcode.com/problems/word-pattern/discuss/1697674/Python-Solution