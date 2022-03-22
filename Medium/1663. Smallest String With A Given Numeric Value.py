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


# Accepted
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        output = ['a'] * n #Since we are forming the lexicographically smallest string, we just simply fill our result with 'a'
        # But, that result will not necessarily have the required score n
        # we can add some 'z' to the back of the result until the score reaches the required value.
        # if we are missing less than 26 to the required score, we add something that is less than 'z'.
        k = k - n 
        i = n - 1
        while k:
            k += 1
            if k//26 >= 1:
                output[i] = 'z'
                k = k - 26
                i -= 1
            else:
                output[i] = chr(k + 96)
                k = 0

        return ''.join(output)
        