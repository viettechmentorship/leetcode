from typing import List


class Solution:
  def stringShift(self, s: str, shift: List[List[int]]) -> str:
    f = 0
    for d, a in shift:
      if d == 0:
        f -= a
      else:
        f += a
    f %= len(s)
    if f == 0:
      return s
    return s[-f:] + s[:-f]
