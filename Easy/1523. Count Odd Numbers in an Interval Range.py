# Problem Statement: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
	# make the low and high variables even numbers so that the return value will be an integer
        if low % 2 == 1:
            low = low - 1
        if high % 2 == 1:
            high = high + 1       
        return int((high-low)/2)