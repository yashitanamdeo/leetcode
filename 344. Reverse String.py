# Problem Statement: https://leetcode.com/problems/reverse-string/

# Method 1
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        
        while start < end:
            s[start], s[end] = s[end], s[start]
            
            start += 1
            end -= 1
        return s

# Method 2
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]

# Method 3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

# Method 4 (similar to method 1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1
        
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            
            start += 1
            end -= 1
        return s