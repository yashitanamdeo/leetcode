# Problem Statement: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        return str(x) == str(x)[::-1]

# Alternate Solution 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        inputNum = x
        newNum = 0
        while x > 0:
            newNum = newNum * 10 + x % 10
            x = x // 10
        return newNum == inputNum

# Alternate Solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
            return False

        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10

        return True if (x == result or x == result // 10) else False
    
'''
Instead of reversing the whole integer, let's convert half of the integer and then check if it's palindrome.
But we don't know when is that half going to come.

Example, if x = 15951, then let's create reverse of x in loop. Initially, x = 15951, revX = 0

x = 1595, revX = 1
x = 159, revX = 15
x = 15, revX = 159
We see that revX > x after 3 loops and we crossed the half way in the integer bcoz it's an odd length integer.
If it's an even length integer, our loop stops exactly in the middle.

Now we can compare x and revX, if even length, or x and revX//10 if odd length and return True if they match.
'''