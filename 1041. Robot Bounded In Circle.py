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

'''
Let's say the robot starts with facing up. It moves [dx, dy] by executing the instructions once.
If the robot starts with facing
right, it moves [dy, -dx];
left, it moves [-dy, dx];
down, it moves [-dx, -dy]

If the robot faces right (clockwise 90 degree) after executing the instructions once,
the direction sequence of executing the instructions repeatedly will be up -> right -> down -> left -> up
The resulting move is [dx, dy] + [dy, -dx] + [-dx, -dy] + [-dy, dx] = [0, 0] (back to the original starting point)

All other possible direction sequences:
up -> left -> down -> right -> up. The resulting move is [dx, dy] + [-dy, dx] + [-dx, -dy] + [dy, -dx] = [0, 0]
up -> down -> up. The resulting move is [dx, dy] + [-dx, -dy] = [0, 0]
up -> up. The resulting move is [dx, dy]
'''

# https://i.imgur.com/asL4A1g.png (direction photo)

# Another Solution
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        rotation = 0
        position = [0,0]
        normal = [0,1]
        for i in instructions:
            if i == "G":
                position[0]+=normal[0]
                position[1]+=normal[1]
                continue
            elif i == "L":
                if rotation == 0:
                    rotation = 270
                else:
                    rotation -=90
            else:
                if rotation == 270:
                    rotation = 0
                else:
                    rotation +=90
            if rotation == 0:
                normal = [0,1]
                continue
            elif rotation == 90:
                normal = [1,0]
                continue
            elif rotation == 180:
                normal = [0,-1]
                continue
            else:
                normal = [-1,0]
                continue
        # after for loop
        if (not position == [0,0]) and normal == [0,1]:
            return False
        return True