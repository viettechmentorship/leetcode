class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = [0] * 26
        ans = 0
        for char in s:
            cnt[ord(char) - 97] += 1
        for freq in cnt:
            if freq > 0:
                if freq % 2 == 1:
                    ans += 1
                else:
                    ans += 2
        return ans