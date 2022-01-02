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