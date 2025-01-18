import queue
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        pq = queue.PriorityQueue()
        pq.put((0, 0, 0))
        while not pq.empty():
            cost, r, c = pq.get()
            if dist[r][c] != cost:
                continue
            for k in range(4):
                u = r + dx[k]
                v = c + dy[k]
                if 0 <= u < rows and 0 <= v < cols:
                    curr = cost
                    if k != grid[r][c] - 1:
                        curr += 1
                    if dist[u][v] > curr:
                        dist[u][v] = curr
                        pq.put((dist[u][v], u, v))
        return dist[rows - 1][cols - 1]            