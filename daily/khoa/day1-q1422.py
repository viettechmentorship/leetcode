class Solution:
  def maxScore(self, s: str) -> int:
    res = count0 = count1 = 0
    for c in s:
      if c == "1":
        count1 += 1
    for i in range(len(s) - 1):
      if s[i] == "0":
        count0 += 1
      else:
        count1 -= 1
      res = max(res, count0 + count1)
    return res
