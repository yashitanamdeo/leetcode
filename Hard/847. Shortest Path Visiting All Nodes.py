# Problem Statement: https://leetcode.com/problems/shortest-path-visiting-all-nodes/

from math import inf
from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        # 1 <= graph.length <= 12
        # 0 <= graph[i].length < graph.length

        nodeCount = len(graph)
        
        # NOTE
        # We are using BFS here because it's better suited for 'shortest path'
        # types of problems. DFS solution is also viable though.

        # Thoughts:
        # 1. start at each node, do BFS to try reaching all other nodes.
        # 2. Must keep track of visited nodes, else infinite loop may happen.
        # 3. But each node may have to be visited multiple times, as described in the problem
        #    statement. So we cannot be too strict in limiting searches
        # 4. We must describe the state during a search, we need:
        #    - The current node we are on
        #    - Nodes we have visited (Notice the order does not matter in this case, that's a key)

        # each search is described by (currentNode, visited)
        # same search does _not_ have to be repeated, since if re-visited with
        # the same state, it would yield the same result.
        # NOTE this does not prevent revisiting the same node again,
        # it just prevents revisiting it with the same STATE!

        # Since the input size is restricted, we can use a number to encode
        # which nodes have been visited -- the i-th bit is on iff node i has been visited

        # conceptually masks[k] indicates that only node k has been visited
        masks = [1 << i for i in range(nodeCount)]
        # used to check whether all nodes have been visited (11111...111)
        allVisited = (1 << nodeCount) - 1
        queue = deque([(i, masks[i]) for i in range(nodeCount)])
        steps = 0

        # encoded_visited in visited_states[node] iff
        # (node, encoded_visited) has been pushed onto the queue
        visited_states = [{masks[i]} for i in range(nodeCount)]
        # states in visited_states will never be pushed onto queue again

        while queue:
            # number of nodes to be popped off for current steps size
            # this avoids having to store steps along with the state
            # which consumes both time and memory
            count = len(queue)

            while count:
                currentNode, visited = queue.popleft()
                if visited == allVisited:
                    return steps

                # start bfs from each neighbor
                for nb in graph[currentNode]:
                    new_visited = visited | masks[nb]
                    # pre-check here to for efficiency, as each steps increment may results
                    # in huge # of nodes being added into queue
                    if new_visited == allVisited:
                        return steps + 1
                    if new_visited not in visited_states[nb]:
                        visited_states[nb].add(new_visited)
                        queue.append((nb, new_visited))

                count -= 1
            steps += 1
        # no path which explores every node
        return inf