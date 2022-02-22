# Problem Statement: https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        for char in columnTitle:
            answer = answer*26 + ord(char)-ord('A')+1
        return answer