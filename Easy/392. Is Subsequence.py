# Problem Statement: https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):return False #if len of s is greater than len of t, return false because s cant be a subsequence of t
        if len(s) == 0:return True
        subsequence=0
        for i in range(0,len(t)):
            if subsequence <= len(s) -1: #if it is matching, increment subsequence
                print(s[subsequence])
                if s[subsequence]==t[i]:

                    subsequence+=1
        return  subsequence == len(s) 

# Alternate Solution
class Solution:
    def isSubsequence(self, s, t):
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True
'''
 If current char is not in t, then we return False
Else, we take the substring of t and start from there
'''