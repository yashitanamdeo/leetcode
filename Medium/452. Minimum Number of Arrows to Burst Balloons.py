# Problem Statement: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda p: p[1])
        ans, arrow = 0, 0
        for [start, end] in points:
            if ans == 0 or start > arrow:
                ans, arrow = ans + 1, end
        return ans