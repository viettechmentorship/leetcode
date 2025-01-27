import queue
class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        total = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != -1:
                    total += grid[i][j]
        
        def dfs(r, c):
            nonlocal curr_sum, curr_component
            curr_sum += grid[r][c]
            curr_component += 1
            grid[r][c] = -1
            for k in range(4):
                u, v = r + dx[k], c + dy[k]
                if 0 <= u < rows and 0 <= v < cols and grid[u][v] > 0:
                    dfs(u, v)

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    curr_sum, curr_component = 0, 0
                    dfs(i, j)
                    ans += (total - curr_sum) * curr_component
        return ans