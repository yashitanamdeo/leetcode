# Problem Statement: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z'}
        len_s, i, ans = len(s), 0, ''
        while i < len_s:
            # Each number between 10 and 26 is followed by # character. 
            # So, If s[i+2] is equal to #, then the number ( e.g. s[i:i+1] ) is between 10 and 26; 
            # otherwise, the number ( e.g. s[i] ) is between 1 and 9.
            if i + 2 < len_s and s[i+2] == '#':
                ans += dic[s[i:i+2]]
                i += 3
            else: 
                ans += dic[s[i]]
                i += 1
        return ans
    
# Alternate Solution
class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = []
        length = len(s)
        
        while i < length:
            if i+2 < length and s[i+2] == '#':
                ans.append(chr(96+int(s[i:i+2])))
                i += 3
            else:
                ans.append(chr(96+int(s[i])))
                i += 1
        
        return ''.join(ans)