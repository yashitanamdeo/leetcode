# Problem Statement: https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n = (num - 3)  // 3
        if 3*n + 3 == num:
            return [n, n+1, n+2]
        return []

# Alternate Solution
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        return [num // 3 - 1, num//3, num//3 + 1]

    
'''
Observe the following:

For num=2. No triplet is possible.
For num=3. Our answer would be: [0, 1, 2].
For num=4. No triplet is possible.
For num=6. Our answer would be: [1, 2, 3].
For num=9. Our answer would be: [2, 3, 4].
Thus, we can say that:

If a number is divisible by 3, then only an answer exists.
If a number is divisible by 3, then it's answer array would have three elements:
i. num/3
ii. num/3 + 1
iii. num/3 - 1

'''