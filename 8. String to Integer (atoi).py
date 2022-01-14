# Problem Statement: https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, s):
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        n, empty, sign = 0, True, 1  # empty denotes we have not seen any number, sign is -1 or 1
        for c in s:
            if empty:
                if c == ' ': continue  # ignore the leading whitespace
                elif c == '-': sign = -1  # final answer is a negative number
                elif c.isdigit(): n = int(c)  # the first digit of number
                elif c != '+': return 0  # the first char is not a digit and not in (' ', '+', '-'), so s is invalid
                empty = False  # the first char is a digit or '+' or '-', valid number starts
            else:
                if c.isdigit():
                    n = n * 10 + int(c)
                    if sign * n > MAX: return MAX
                    elif sign * n < MIN: return MIN
                else: break   # end of valid number
        return sign * n  # sign is 1 or -1 