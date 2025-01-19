class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ans = 0
        rows, cols = len(heightMap), len(heightMap[0])
        visit = [[False] * cols for _ in range(rows)]
        pq = []
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    visit[i][j] = True
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        while pq:
            height, r, c = heapq.heappop(pq)
            for k in range(4):
                u = r + dx[k]
                v = c + dy[k]
                if 0 <= u < rows and 0 <= v < cols and not visit[u][v]:
                    if heightMap[u][v] < height:
                        ans += height - heightMap[u][v]
                        heapq.heappush(pq, (height, u, v))
                    else:
                        heapq.heappush(pq, (heightMap[u][v], u, v))
                    visit[u][v] = True
        return ans