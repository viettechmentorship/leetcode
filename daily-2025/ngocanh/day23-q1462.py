class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        ans = []
        def dfs(node, target):
            visit[node] = True
            if node == target:
                return True
            for neighbor in graph[node]:
                if not visit[neighbor]:
                    if dfs(neighbor, target):
                        return True
            return False
        for a, b in queries:
            visit = [False] * numCourses 
            ans.append(dfs(a, b))
        return ans