import queue
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        rows, cols = len(isWater), len(isWater[0])
        ans = [[-1] * cols for _ in range(rows)]
        q = queue.Queue()
        curr_height = 1
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    ans[i][j] = 0
                    q.put((i, j))
        while not q.empty():
            size = q.qsize()
            for _ in range(size):
                r, c = q.get()
                for k in range(4):
                    u = r + dx[k]
                    v = c + dy[k]
                    if 0 <= u < rows and 0 <= v < cols and ans[u][v] == -1:
                        ans[u][v] = curr_height
                        q.put((u, v))
            curr_height += 1
        return ans
