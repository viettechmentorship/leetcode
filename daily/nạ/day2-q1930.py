class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_idx = [-1] * 26
        last_idx = [-1] * 26
        for i in range(len(s)):
            if first_idx[ord(s[i]) - 97] == -1:
                first_idx[ord(s[i]) - 97] = i
            last_idx[ord(s[i]) - 97] = i
            
        ans = 0
        for i in range(26):
            if first_idx[i] == -1:
                continue
            sub_str = set()
            for j in range(first_idx[i] + 1, last_idx[i]):
                sub_str.add(s[j])
            ans += len(sub_str)
        return ans 