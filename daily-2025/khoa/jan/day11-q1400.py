class Solution:
  def canConstruct(self, s: str, k: int) -> bool:
    f = {}
    for c in s:
      f[c] = f.get(c, 0) + 1
    odd = 0
    for c in f:
      if f[c] % 2 == 1:
        odd += 1
    return odd <= k and len(s) >= k
