# Problem Statement: https://leetcode.com/problems/robot-bounded-in-circle/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y,dx,dy = 0,0,0,1
        for i in instructions:
            if i == 'G':
                x,y = x+dx,y+dy
            if i == 'L':
                dx,dy = -dy, dx
            if i == 'R':
                dx,dy = dy, -dx
        return (x,y) == (0,0) or (dx,dy) != (0,1)