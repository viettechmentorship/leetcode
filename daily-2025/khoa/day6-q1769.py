from typing import List


class Solution:
  def minOperations(self, boxes: str) -> List[int]:
    cl = vl = cr = vr = 0
    n = len(boxes)
    for i in range(1, n):
      if boxes[i] == "1":
        cr += 1
        vr += i
    res = [0] * n
    res[0] = vr
    for i in range(1, n):
      vr -= cr
      if boxes[i] == "1":
        cr -= 1
      if boxes[i - 1] == "1":
        cl += 1
      vl += cl
      res[i] = vr + vl
    return res
