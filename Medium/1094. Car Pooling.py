# Problem Statement: https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1001
        for number,start,end in trips:
            timestamp[start] += number
            timestamp[end] -= number
        size = 0
        for item in timestamp:
            size += item
            if size > capacity:
                return False
        return True