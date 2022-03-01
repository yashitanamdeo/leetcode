# Problem Statement: https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        def toBinary(num):
             return bin(num).replace("0b", "")
        
        binary_num = []
        for i in range(n+1):
            num = toBinary(i)
            binary_num.append(str(num))
        
        answer = []
        for element in binary_num:
            count = 0
            for digit in element:
                if digit == '1':
                    count += 1
            answer.append(count)
        return answer