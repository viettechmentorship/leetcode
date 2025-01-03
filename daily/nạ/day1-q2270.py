class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_left = [0] * (len(nums))
        prefix_right = [0] * (len(nums))
        for i in range(len(nums)):
            prefix_left[i] = prefix_left[i - 1] + nums[i]
        prefix_right[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            prefix_right[i] = prefix_right[i + 1] + nums[i]
        ans = 0
        for i in range(len(prefix_left) - 1):
            if prefix_left[i] >= prefix_right[i + 1]:
                ans += 1
        return ans