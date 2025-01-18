import queue
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        rows, cols = len(grid), len(grid[0])
        visit = [[False] * cols for _ in range(rows)]
        dist = [[float('inf')] * cols for _ in range(rows)]
        
        def bfs(row, col):
            q = queue.Queue()
            q.put((row, col, 0))
            visit[row][col] = True
            dist[row][col] = 0
            while not q.empty():
                r, c, cost = q.get()
                for k in range(4):
                    u = r + dx[k]
                    v = c + dy[k]
                    if 0 <= u < rows and 0 <= v < cols and not visit[u][v] and grid[u][v] != 'X':
                        visit[u][v] = True
                        dist[u][v] = cost + 1
                        q.put((u, v, dist[u][v]))
            return dist 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    dist = bfs(i, j)
        ans = float('inf')
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '#':
                    ans = min(ans, dist[i][j])
        return ans if ans != float('inf') else -1