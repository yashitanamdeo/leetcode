# Problem Statement: https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        if len(word1) == len(word2):
            for i in range(len(word1)):
                ans = ans + word1[i] + word2[i]
            return ans
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                ans = ans + word1[i] + word2[i]
            ans = ans + word2[i+1:]
            return ans
        else:
            for i in range(len(word2)):
                ans = ans + word1[i] + word2[i]
            ans = ans + word1[i+1:]
            return ans
        
# Alternate Solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ''
        for i in range(min(len(word1),len(word2))):
            mergedString += word1[i] + word2[i]
            
        return mergedString + word1[i+1:] + word2[i+1:]