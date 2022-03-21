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
    
'''
Since each letter can appear only in one part, we cannot form a part shorter than the 
index of the last appearance of a letter subtracted by an index of the first appearance. 
For example here (absfab) the lengths of the first part are limited by the positions of the letter a. 
So it's important to know at what index each letter appears in the string last time. 
We can create a hash map and fill it with the last indexes for letters.

Also, we have to validate a candidate part. 
For the same example (absfab) we see that letter a cannot form a border for the first part 
because of a nasty letter b inside. So we need to expand the range of the initial part.
'''