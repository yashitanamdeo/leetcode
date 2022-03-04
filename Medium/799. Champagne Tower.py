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

'''
What we need to do in this problem is to simulate our pouring process: imagine, that we have 6 cups of water arrived at some place, then one full cup is left on this place and 2.5 cups go to the right bottom and left bottom cups. What we need to do now is to simulate this process!

1. We start with l = [poured] - top layer
2. Then we process full current layer to create next layer. We need to check if we have enough champagne: if we have less than 1, this cup is dead-end. If it has more than 1, then we add values to bottom layer.
'''