# Problem Statement: https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack:

    def __init__(self):
        self.heap = []
        self.m = collections.defaultdict(int)
        self.counter = 0
        
    def push(self, val):
        self.m[val]+=1
        heapq.heappush(self.heap,(-self.m[val], -self.counter, val))
        self.counter+=1
    
    def pop(self):
        toBeRemoved = heapq.heappop(self.heap)
        self.m[toBeRemoved[2]]-=1
        return toBeRemoved[2]
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()