from typing import List


class Solution:
  def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    ps = [0]
    vowels = "aeiou"
    for w in words:
      if w[0] in vowels and w[-1] in vowels:
        ps.append(ps[-1] + 1)
      else:
        ps.append(ps[-1])
    res = []
    for l, r in queries:
      res.append(ps[r + 1] - ps[l])
    return res
    return res
