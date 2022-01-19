# Problem Statement: https://leetcode.com/problems/jump-game-iv/

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        visited = set()
        xs = defaultdict(list)
        for i, v in enumerate(arr):
            xs[v].append(i)
        
        N = len(arr)
        if N == 1:
            return 0

        
        num_steps = 1
        level = [N-1]
        visited.add(N-1)

        while level:
            next_level = set()
            # print(level, num_steps)
            
            for i in level:
                if i == 1:
                    return num_steps
                
                if i-1 not in visited:
                    visited.add(i-1)
                    next_level.add(i-1)
                if i != N-1 and i+1 not in visited:
                    visited.add(i+1)
                    next_level.add(i+1)
                
                for ni in xs[arr[i]]:
                    if ni == 0:
                        return num_steps
                    if ni not in visited:
                        visited.add(ni)
                        next_level.add(ni)
            
            num_steps += 1
            level = next_level