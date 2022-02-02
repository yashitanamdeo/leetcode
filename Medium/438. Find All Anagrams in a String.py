# Problem Statement: https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]: 
        # take counter of first n elements in s_dict with n = len(p) - 1
        s_dict = collections.Counter(s[:len(p)-1]) 
        # counter of p, this should not be changed
        p_dict = collections.Counter(p)
        start = 0
        # final result list
        result = []
        # We iterate over the string s, and in each step we check if s_dict and p_dict match
        for i in range(len(p)-1, len(s)):
            # updating the counter & adding the character
            s_dict[s[i]] += 1
            # checking if counters match
            if s_dict == p_dict:
                result.append(start)
            # remove the first element from counter
            s_dict[s[start]] -= 1
            #if element count = 0, pop it from the counter
            if s_dict[s[start]] == 0:
                del s_dict[s[start]]
            start += 1
            
        return result