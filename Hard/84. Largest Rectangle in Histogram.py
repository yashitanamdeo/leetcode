#Problem Statement: https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, bars: List[int]) -> int:
        st, res = [], 0
        for bar in bars + [-1]: # add -1 to have an additional iteration
            step = 0
            while st and st[-1][1] >= bar:
                w, h = st.pop()
                step += w
                res = max(res, step * h)

            st.append((step + 1, bar))

        return res