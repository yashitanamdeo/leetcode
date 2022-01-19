# Problem Statement: https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        no_of_trust = [0] * (n+1) #because in trust numbers starts from 1 to N
        for a,b in trust:
            no_of_trust[a] -= 1 # a trusts b so a will become less
            no_of_trust[b] += 1 # a trusts b so b will become more trustworthy.
            
        for i in range(1,n+1): #because values are modified in range of 1 to N only
            if no_of_trust[i] == n-1: # n-1 is the higghest possible value if a judge is present
                return i #return the index where judge is found
        return -1