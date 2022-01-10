# Problem Statement: https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        # zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        result = ''
  
        carry = 0
  
        # Traversing string
        for i in range(max_len - 1, -1, -1):
            r = carry
            if a[i] == '1':
                r += 1 
            else:
                r += 0
            if b[i] == '1':
                r += 1
            else:
                r += 0
            if r % 2 == 1:
                result = '1' + result
            else:
                result = '0' + result
            

            # Computing carry.
            carry = 0 if r < 2 else 1

        if carry != 0:
            result = '1' + result
        return result