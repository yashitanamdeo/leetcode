# Problem Statement: https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/"

# Time Limit Exceeded
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        alphabets = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        output = ''
        for i in range(n,0,-1):
            value = k - (i - 1)
            if value >= 26:
                output = alphabets[26] + output
                k -= 26
            else:
                output = alphabets[value] + output
                k -=  value
        return output
