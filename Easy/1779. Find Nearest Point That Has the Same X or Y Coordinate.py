# Problem Statement: https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        m = 10000
        for i in points:
            if i[0] == x or i[1] == y:
                if m > abs(x-i[0]) + abs(y-i[1]):
                    m = min(m,abs(x-i[0])+abs(y-i[1]))
                    o = points.index(i)
        if m == 10000:
            return -1
        return o