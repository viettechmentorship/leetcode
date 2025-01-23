class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0 
        rows = [0] * (len(grid[0]))
        cols = [0] * (len(grid))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[j] += 1
                    cols[i] += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if rows[j] > 1 or cols[i] > 1:
                        ans += 1
        return ans 