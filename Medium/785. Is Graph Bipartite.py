# Problem Statement: https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def checkBipartite(vertex):
            nonlocal color
            nonlocal q

            q.append(vertex)
            color[vertex] = 1

            while(q):
                curr = q.popleft()

                for i in graph[curr]:
                    if color[i] == -1:
                        color[i] = 1-color[curr]
                        q.append(i)
                    else:
                        if color[i] == color[curr]:
                            return False
            return True
        color = [-1]*len(graph)
        q = collections.deque()
        for i in range(len(graph)):
            if color[i] == -1:
                if not checkBipartite(i):
                    return False
        return True
