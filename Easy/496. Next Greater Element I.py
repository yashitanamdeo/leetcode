# Problem Statement: https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_map = {x : -1 for x in nums1} 
        stack = []
		
        for num in nums2:
            while stack and stack[-1] < num:
                prev_num = stack.pop()
                if prev_num in greater_map:
                    greater_map[prev_num] = num
            stack.append(num)
            
        return [greater_map[x] for x in nums1]