# Problem Statement: https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Populating the directions array
        # Corresponding to [N, NE, E, SE, S, SW, W, NW]
        directions = [[-1,0], [-1,1], [0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                # Maintaining a counter of live cells in the original matrix
                livecount = 0
                
                for direction in directions:
                    # Determining what our new row would be after taking a direction
                    nr = i + direction[0]
                    
                    # Determining what our new column would be after taking a direction
                    nc = j + direction[1]
                    
                    # Ensuring that our new_row and new_column
                    # are within the bounds of the matrix
                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc])==1:
                        livecount += 1
                
                if board[i][j] == 1:
                    # case where live cell dies from under/over population
                    if livecount<2 or livecount>3:
                        board[i][j] = -1
                else:
                    # case of dead cell resurrection
                    if livecount==3:
                        board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1