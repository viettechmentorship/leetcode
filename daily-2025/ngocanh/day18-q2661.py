class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        cnt_cols = [0] * (cols)
        cnt_rows = [0] * (rows)
        position = {}
        for i in range(rows):
            for j in range(cols):
                position[mat[i][j]] = (i, j)
        
        for i in range(len(arr)):
            num = arr[i]
            pos = position[num]
            cnt_cols[pos[1]] += 1
            cnt_rows[pos[0]] += 1
            if cnt_cols[pos[1]] == rows or cnt_rows[pos[0]] == cols:
                return i