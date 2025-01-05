from typing import List


class Solution:
  def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    n = len(s)
    delta = [0] * n
    for l, r, d in shifts:
      d = 1 if d == 1 else -1
      delta[l] += d
      if r + 1 < n:
        delta[r + 1] -= d
    for i in range(1, n):
      delta[i] += delta[i - 1]
    res = []
    for i in range(n):
      offset = (ord(s[i]) - ord("a") + delta[i]) % 26
      res.append(chr(offset + ord("a")))
    return "".join(res)
