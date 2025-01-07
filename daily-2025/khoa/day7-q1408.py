from typing import List


class Solution:
  def stringMatching(self, words: List[str]) -> List[str]:
    res = set()
    for a in words:
      for b in words:
        if a != b and a.find(b) != -1:
          res.add(b)
    return list(res)
