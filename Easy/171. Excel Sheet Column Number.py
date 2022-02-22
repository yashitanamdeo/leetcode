# Problem Statement: https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        for char in columnTitle:
            answer = answer*26 + ord(char)-ord('A')+1
        return answer


# Alternate Solution
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter)-64
            ans += digit * 26**pos
            pos += 1
            
        return ans

'''
Essentially, what we asked to do here is to convert a number in the base 26 numeral system 
to a decimal number. This is a standard algorithm, where we iterate over the digits from 
right to left and multiply them by the base to the power of the position of the digit. 
To translate a letter to a number we use the Python method ord which returns the Unicode code of the letter. 
By subtracting the code by 64, we can map letters to the numbers from 1 to 26.

26**pos because:
eg: number = '2539'
ans = ans + 9 * 10**0
ans = ans + 3 * 10**1
ans = ans + 5 * 10**2
ans = ans + 2 * 10**3
ans = 2539
For base 26 we do absolutely the same but instead of 10 we use 26.
'''