# Problem Statement: https://leetcode.com/problems/path-with-minimum-effort/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0

        r, c = len(heights), len(heights[0])
        heap = [(0,0,0)]
        res = 0
        visited = set()

        while heap:
            # Always pop up the smaller abs distance 
            d, x, y = heapq.heappop(heap)

            res = max(res, d)
            if (x, y) == (r-1, c-1):
                return res
            visited.add((x, y))

            for nx, ny in (x+1, y), (x-1,y), (x, y+1), (x, y-1):
                if nx >= 0 and nx < r and ny >= 0 and ny < c and (nx, ny) not in visited:
                    nd = abs(heights[nx][ny] - heights[x][y])
                    heapq.heappush(heap, (nd, nx, ny))

        return res