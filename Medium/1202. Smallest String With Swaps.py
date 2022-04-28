# Problem Statement: https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        d = defaultdict(list)
        for a,b in pairs:
            d[a].append(b)
            d[b].append(a)
        
        def dfs(x,A):
            if x in d:
                A.append(x)
                for y in d.pop(x):
                    dfs(y,A)
        
        s    = list(s)
        while d:
            x = next(iter(d))
            A = []
            dfs(x,A)
            A = sorted(A)
            B = sorted([ s[i] for i in A ])
            for i,b in enumerate(B):
                s[A[i]] = b
        return ''.join(s)
    
'''
1. The initial idea is that each pair of swappable letters in "pairs" can be treated as an edge in a (undirected) graph. This works because, in the limit case, we could do bubble sort across connected letters.

2. We then go one step further and treat each index s[i] as a node, and convert the array "pairs" into a dictionary "d" of connected nodes.

3. While our dictionary "d" has entries, we choose one element in "d" and visit all connected nodes, returning a list of detected points. We sort this list, and place the results back in our final string/array. Since each node can only be visited once, this process has a linear time complexity of O(E), where E is the number of edges in our graph ( E = len(pairs) ).

4. Once all nodes have been visited, we exit our function and return the final string, with all its connected sections sorted .
'''