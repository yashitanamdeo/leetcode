# Problem Statement: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

from collections import defaultdict

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        counterT = defaultdict(int) #count of the occurences of numbers in tops
        counterB = defaultdict(int) #count of the occurences of numbers in buttoms
        same = 0 #counting the same occurences in top & bottom
        
        for i in range(len(tops)):
            counterT[tops[i]] += 1
            counterB[bottoms[i]] += 1
            
            if tops[i] == bottoms[i]:
                same += 1
                
        for num in range(1,7):
            if (counterT[num] + counterB[num] - same) == len(tops):
                return len(tops) - max(counterT[num],counterB[num])
        
        return -1
    
    '''
    If we can make number i in a whole row it should satisfy that counterT[i] + counterB[i] - same == len(top) or len(bottom)
    
    eg in the first test Case:
        tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
        faceA[2] = 4 , as tops[0] = tops[2] = tops[4] = tops[5]
        faceB[2] = 3, as bottoms[1] = bottoms[3] = bottoms[5]
        same[2] = 1, as tops[5] = bottoms[5]
        Therefore we have faceA[2] + faceB[2] - same[2] = 6, (size of arr)
        Therfore we can make 2 in a whole row.
    '''