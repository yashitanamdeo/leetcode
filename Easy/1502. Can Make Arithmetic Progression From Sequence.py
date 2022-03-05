# Problem Statement: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        difference = arr[1] - arr[0]
        ans = False
        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) == difference:
                ans = True
            else:
                ans = False
                return ans
        return ans