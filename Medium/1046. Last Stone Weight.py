# Problem Statement: https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_stones = sorted(stones)
        while len(sorted_stones) > 1:
            stone1 = sorted_stones.pop() #highest
            stone2 = sorted_stones.pop() #second highest
            if stone2 != stone1:
                sorted_stones.append(stone1-stone2)
                sorted_stones = sorted(sorted_stones)
        if sorted_stones:
            return sorted_stones[0]
        return 0