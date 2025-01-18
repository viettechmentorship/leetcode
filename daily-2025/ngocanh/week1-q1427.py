"""
[0, 1], [1, 2]
+1 - 2 = -1
"""
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        curr_sum = 0
        for dir, num in shift:
            if dir == 0:
                curr_sum += num
            else:
                curr_sum -= num
        curr_sum %= len(s)
        return s[curr_sum:] + s[:curr_sum]