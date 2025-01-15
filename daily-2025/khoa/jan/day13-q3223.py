class Solution:
  def minimumLength(self, s: str) -> int:
    count = {}
    for c in s:
      count[c] = count.get(c, 0) + 1
    res = 0
    for k in count:
      if count[k] >= 3:
        if count[k] % 2 == 0:
          res += 2
        else:
          res += 1
      else:
        res += count[k]
    return res
