from typing import List


class Solution:
  def waysToSplitArray(self, nums: List[int]) -> int:
    total = sum(nums)
    res = cumulative = 0
    for i in range(len(nums) - 1):
      cumulative += nums[i]
      if cumulative >= total - cumulative:
        res += 1
    return res
    return res
