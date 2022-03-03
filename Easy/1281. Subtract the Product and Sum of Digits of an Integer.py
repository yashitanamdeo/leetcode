# Problem Statement: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_of_digits = 1
        sum_of_digits = 0
        n = str(n)
        for digit in n:
            product_of_digits *= int(digit)
            sum_of_digits += int(digit)
        
        return product_of_digits - sum_of_digits