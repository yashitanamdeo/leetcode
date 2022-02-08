# Problem Statement: https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: 
            return 0
        if num % 9 == 0: 
            return 9
        else: 
            return(num % 9)

# Alternate Solution 1
'''
def Sum(a):
    ans = 0
    for i in str(a):
        ans += int(i)
    return ans    

class Solution:
    def addDigits(self, num: int) -> int:
        sum = Sum(num)
        if len(str(sum)) == 1:
            return sum
        while len(str((sum))) != 1:
            sum = Sum(sum)
            if len(str(sum)) == 1:
                return sum
'''

# Alternate Solution 2

'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num//10 == 0:
            return num
        
        sum = 0
        while num > 0:
            sum += num%10
            num = num//10
            
        return self.addDigits(sum) 
    
    # OR THIS WAY
        while(num >= 10):
            temp = 0
            while(num > 0):
                temp += num % 10
                num = num // 10
            num = temp
        return num
'''