# Problem Statement: https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        l = [poured]
        for _ in range(query_row):
            l_new = [0] * (len(l) + 1)
            for i in range(len(l)):
                pour = (l[i] - 1)/2
                if pour > 0:
                    l_new[i] += pour
                    l_new[i+1] += pour
            
            l = l_new
                    
        return min(1, l[query_glass])

