from typing import List


class Solution:
  def countPrefixSuffixPairs(self, words: List[str]) -> int:
    n = len(words)
    res = 0
    for i in range(n):
      for j in range(i + 1, n):
        a, b = words[i], words[j]
        na, nb = len(a), len(b)
        if na > nb:
          continue
        if b[:na] == a and b[-na:] == a:
          res += 1
    return res
