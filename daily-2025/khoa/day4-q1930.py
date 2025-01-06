class Solution:
  def countPalindromicSubsequence(self, s: str) -> int:
    first, last = [None] * 26, [None] * 26
    count = []
    for i in range(len(s)):
      k = ord(s[i]) - ord("a")
      if first[k] is None:
        first[k] = i
      last[k] = i
      if not count:
        count.append([0] * 26)
      else:
        count.append(count[-1].copy())
      count[-1][k] += 1
    res = 0
    for i in range(26):
      if first[i] is None or last[i] is None or first[i] == last[i]:
        continue
      a, b = first[i], last[i]
      for j in range(26):
        if count[b - 1][j] - count[a][j] > 0:
          res += 1
    return res
