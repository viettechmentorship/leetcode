class Solution:
  def equalDigitFrequency(self, s: str) -> int:
    n = len(s)
    res = 0
    seen = set()
    for i in range(n):
      count = [0] * 10
      for j in range(i, n):
        count[int(s[j])] += 1
        maxf = max(count)
        if all(c == 0 or c == maxf for c in count) and s[i : j + 1] not in seen:
          seen.add(s[i : j + 1])
          res += 1
    return res
