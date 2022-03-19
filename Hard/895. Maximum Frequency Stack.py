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
        
''' Heap will always keep the element with max count on top, and if two elements have same count, 
the second element (index) will be considered while doing pop operation. 
Also, the count map, is useful when the new occurence of the exisiting element is pushed.'''

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()