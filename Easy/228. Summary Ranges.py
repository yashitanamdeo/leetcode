# Problem Statement: https://leetcode.com/problems/summary-ranges/

class Solution:
	def summaryRanges(self, nums: List[int]) -> List[str]:
		start = 0
		end = 0
		result = []
		while start < len(nums) and end<len(nums):
			if end+1 < len(nums) and nums[end]+1 == nums[end+1]:
				end=end+1
			else:
				if start == end:
					result.append(str(nums[start]))
					start = start + 1
					end = end + 1
				else:
					result.append(str(nums[start])+'->'+str(nums[end]))
					start = end + 1
					end = end + 1
		return result