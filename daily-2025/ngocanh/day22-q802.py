import queue
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        in_degree = [0] * (len(graph))
        adj = [[] for _ in range(len(graph))]
        for i in range(len(graph)):
            for node in graph[i]:
                adj[node].append(i)
                in_degree[i] += 1
        q = queue.Queue()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.put(i)
        ans = []
        while not q.empty():
            node = q.get()
            ans.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.put(neighbor)
        return sorted(ans)