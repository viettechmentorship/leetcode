from typing import List


class Solution:
  def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
    n = len(A)
    count, res = 0, []
    seen = set()
    for i in range(n):
      if A[i] not in seen:
        seen.add(A[i])
      else:
        seen.remove(A[i])
        count += 1
      if B[i] not in seen:
        seen.add(B[i])
      else:
        seen.remove(B[i])
        count += 1
      res.append(count)
    return res
    return res
