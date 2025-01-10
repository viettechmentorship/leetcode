from typing import List


class Solution:
  def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    def count(w):
      f = {}
      for c in w:
        f[c] = f.get(c, 0) + 1
      return f

    def subset(fa, fb):
      if len(fa) < len(fb):
        return False
      for k in fb:
        if k not in fa or fa[k] < fb[k]:
          return False
      return True

    res, f2 = [], {}
    for w in words2:
      f = count(w)
      for k in f:
        f2[k] = max(f2.get(k, 0), f[k])
    chars = sum(f2.values())

    for w in words1:
      if len(w) < chars:
        continue
      f1 = count(w)
      if len(f1) < len(f2):
        continue
      for k in f2:
        if k not in f1 or f1[k] < f2[k]:
          break
      else:
        res.append(w)
    return res
