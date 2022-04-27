# Problem Statement: https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        d = defaultdict(list)
        for a,b in pairs:
            d[a].append(b)
            d[b].append(a)
        #
        def dfs(x,A):
            if x in d:
                A.append(x)
                for y in d.pop(x):
                    dfs(y,A)
        #
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