class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        cnt = {}
        for num in nums1:
            cnt[num] = cnt.get(num, 0) + len(nums2)
        for num in nums2:
            cnt[num] = cnt.get(num, 0) + len(nums1)
        ans = 0
        for num, freq in cnt.items():
            if freq % 2 == 1:
                ans ^= num
        return ans