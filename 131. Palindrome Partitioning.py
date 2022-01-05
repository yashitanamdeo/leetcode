# Problem Statement: https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []
        
        def dfs(i):
            if i >= len(s):
                result.append(partition.copy())
                return
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    partition.append(s[i:j+1])
                    dfs(j + 1)
                    partition.pop()
        dfs(0)
        return result
    
    def isPalindrome(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l,r = l+1,r-1
        return True