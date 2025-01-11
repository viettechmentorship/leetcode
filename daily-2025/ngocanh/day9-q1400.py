class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        cnt = Counter(s)
        odd_cnt = 0
        for char, freq in cnt.items():
            if freq % 2 == 1:
                odd_cnt += 1
        if k < odd_cnt or k > len(s):
            return False
        else:
            return True