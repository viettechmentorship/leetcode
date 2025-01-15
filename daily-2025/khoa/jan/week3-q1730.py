from collections import deque
from typing import List


class Solution:
  def getFood(self, grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    ci = cj = None
    for i in range(m):
      for j in range(n):
        if grid[i][j] == "*":
          ci, cj = i, j
          break
    q = deque()
    q.append((ci, cj, 0))
    grid[ci][cj] = "!"
    while q:
      ci, cj, d = q.popleft()
      for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < m and 0 <= nj < n:
          if grid[ni][nj] == "#":
            return d + 1
          if grid[ni][nj] == "O":
            grid[ni][nj] = "!"
            q.append((ni, nj, d + 1))
    return -1
