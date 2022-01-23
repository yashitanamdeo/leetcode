# Problem Statement: https://leetcode.com/problems/sequential-digits/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = list()

        for window in range(floor(log10(low)) + 1, floor(log10(high)) + 2):
            for start in range(10 - window):
                number = 0
                for i in range(start, start + window):
                    number = number * 10 + i + 1

                if low <= number <= high: 
                    result.append(number)

        return result