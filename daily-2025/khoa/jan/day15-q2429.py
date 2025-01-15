class Solution:
  def minimizeXor(self, num1: int, num2: int) -> int:
    count1 = 0
    while num2:
      count1 += num2 % 2
      num2 //= 2
    b1 = []
    while num1:
      b1.append(num1 % 2)
      num1 //= 2
    b1.reverse()
    res = [0] * max(len(b1), count1)
    n = len(res)
    offset = n - len(b1)

    for i in range(len(b1)):
      if count1 == 0:
        break
      if b1[i] == 1:
        count1 -= 1
        b1[i] = 0
        res[offset + i] = 1
    for i in range(n - 1, -1, -1):
      if count1 == 0:
        break
      if res[i] == 0:
        count1 -= 1
        res[i] = 1
    val = 0
    for i in range(n):
      val = val * 2 + res[i]
    return val
