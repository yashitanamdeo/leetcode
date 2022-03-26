# Problem Statement: https://leetcode.com/problems/binary-search/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #corner case: nums is empty
        if not nums or len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        #corner case: target value is out of the list's value range
        if target < nums[left] or target > nums[right]:
            return -1
        #lock the target in left, right and mid three numbers.
        while left + 1 < right:     
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                return mid    
        #if the target is not the mid, check the right and left
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1