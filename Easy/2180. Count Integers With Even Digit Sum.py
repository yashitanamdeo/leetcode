# Problem Statement: https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(num+1):
            sum_of_digits = sum(int(digit) for digit in str(i)) 
            if sum_of_digits % 2 == 0 and sum_of_digits != 0:
                count += 1
        return count
        #return sum(sum(int(x) for x in str(i)) % 2 == 0 for i in range(2, num + 1))