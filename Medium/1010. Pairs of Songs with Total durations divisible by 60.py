# Problem Statement: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

# Brute Force : Complexity - O(n^2)
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        for i in range(0,len(time)-1):
            for j in range(i+1,len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        return count

# Using HashMap i.e dictionary : Complexity - O(n)
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        HashMap = {}
        pairs = 0
        
        for t in time:
            numMod = t % 60
            
            if numMod == 0:
                if 0 in HashMap:
                    pairs += HashMap[0]
            elif (60 - numMod) in HashMap:
                pairs += HashMap[60 - numMod]
                
            if numMod in HashMap:
                HashMap[numMod] += 1
            else:
                HashMap[numMod] = 1
                
        return pairs
                