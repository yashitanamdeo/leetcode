# Problem Statement: https://leetcode.com/problems/remove-covered-intervals/

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        start, end = 0, 1
        # Sort by left bound, and reversed right bound of interval
        intervals.sort(key = lambda segment:(segment[start], -segment[end]) )
        # count of non-covered intervals
        count = 0
		# right bound so far
        right_bound = 0
        for interval in intervals:
            if right_bound < interval[end]:
                # previous interval can not cover current interval, update count
                count, right_bound = count + 1, interval[end]
        return count