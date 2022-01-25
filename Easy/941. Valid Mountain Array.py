# problem Statement: https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        left = 0
        right = len(arr) - 1
        while left + 1 < len(arr) - 1 and arr[left] < arr[left + 1]: 
            left += 1
        while right - 1 > 0 and arr[right] < arr[right - 1]: 
            right -= 1
        return left == right