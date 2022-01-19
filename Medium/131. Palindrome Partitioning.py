# Problem Statement: https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = [] # will store all posible partitions
        partition = [] # current partition
        
        # function for backtracking
        def dfs(i): # i is the index of the character we are currently at
            if i >= len(s): # checking base case
                result.append(partition.copy()) 
                ''' because there is only 1 partition variable and we will keep updating/changing it 
                    so we need to copy it everytime we append to result '''
                return
            for j in range(i,len(s)): # generating every single possible substring
                if self.isPalindrome(s,i,j): # checking is the substring is palindrome
                    partition.append(s[i:j+1])
                    dfs(j + 1) # recursively continue our dfs
                    partition.pop()
                # if a substring is not a palindrome, we just skip it
        dfs(0)
        return result
    
    # function for palindrome checking
    def isPalindrome(self,s,left,right): 
        while left < right:
            if s[left] != s[right]: # if character at left position doesnot equal character at left position
                return False # substring is not palindrom
            left,right = left+1,right-1 # if they are equal we update left and right pointers
        return True # substring is palindrome