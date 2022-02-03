# Problem Statement: https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        # hashmap and final result count
        nums12, result = defaultdict(int), 0
        
        # storing all possible combinations of sum
        for num1 in nums1:
            for num2 in nums2:
                nums12[num1+num2] += 1
        
        # iterating the left out two array to find negation of same value
        for num3 in nums3:
            for num4 in nums4:
                result += nums12[-(num3+num4)]
        
        return result