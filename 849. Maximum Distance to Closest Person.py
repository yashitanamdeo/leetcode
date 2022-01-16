# Problem Statement: https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        distance = -1 
        Maximum_Distance = 0
        for i in range(len(seats)):
            if seats[i] == 1: # if seat is 0 that means it is empty we won't perform any action
                if distance == -1: # if we are encounting the first seated person
                    Maximum_Distance = i 

                else:
                    Maximum_Distance = max(Maximum_Distance,((i - distance) // 2)) 
                    # if we have encounted any seated person before then we will compare for the maximum distance till now to the current distance possible
                
                distance = i 

        if seats[-1] == 0: # if end seat is empty
            Maximum_Distance = max(Maximum_Distance, (len(seats) - 1 - distance))
        return Maximum_Distance
                
# Post: https://leetcode.com/problems/maximize-distance-to-closest-person/discuss/1694631/Python-O(n)-Solution-with-comments