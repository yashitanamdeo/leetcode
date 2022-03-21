# Problem Statement: https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {s[i]: i for i in range(len(s))} # last appearance of the letter
        i, ans = 0, []
        while i < len(s):
            end, j = last[s[i]], i + 1
            while j < end: # validation of the part [i, end]
                if last[s[j]] > end:
                    end = last[s[j]] # extend the part
                j += 1
           
            ans.append(end - i + 1)
            i = end + 1
            
        return ans