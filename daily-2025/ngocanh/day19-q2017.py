class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top = sum(grid[0])
        ans = float('inf')
        bottom = 0
        for i in range(len(grid[0])):
            top -= grid[0][i]
            ans = min(ans, max(top, bottom))
            bottom += grid[1][i]
        return ans