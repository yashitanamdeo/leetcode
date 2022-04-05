# Problem Statement: https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        l, r, area = 0, len(height) - 1, 0
        while l < r:
            min_height=min(height[l], height[r])
            area = max(area, (r - l) * min_height)
            if height[l] < height[r]:
                l+=1
                while height[l]<min_height:
                    l+=1
            else:
                r-=1
                while height[r]<min_height:
                    r-=1			
        return area