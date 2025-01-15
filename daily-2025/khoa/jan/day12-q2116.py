class Solution:
  def canBeValid(self, s: str, locked: str) -> bool:
    n = len(s)
    if n % 2 == 1:
      return False
    left = uncertain = 0
    for i in range(n):
      if locked[i] == "0":
        uncertain += 1
      elif s[i] == "(":
        left += 1
      elif left > 0:
        left -= 1
      elif uncertain > 0:
        uncertain -= 1
      else:
        return False
    right = uncertain = 0
    for i in range(n - 1, -1, -1):
      if locked[i] == "0":
        uncertain += 1
      elif s[i] == ")":
        right += 1
      elif right > 0:
        right -= 1
      elif uncertain > 0:
        uncertain -= 1
      else:
        return False
    return True
