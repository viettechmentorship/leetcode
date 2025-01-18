class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        ans = set()
        mod = 10**9 + 7
        def compute_powers(n):
            powers = [1] * (n + 1)
            for i in range(1, n + 1):
                powers[i] = (powers[i - 1] * 33) % mod
            return powers 
        
        def func_hash(str):
            hash_value = [0] * (len(str) + 1)
            for i in range(len(str)):
                hash_value[i + 1] = (hash_value[i] * 33 + ord(str[i])) % mod
            return hash_value
        
        powers = compute_powers(len(s))
        hash_value = func_hash(s)
        for i in range(len(s)):
            freq = [0] * 10
            for j in range(i, len(s)):
                digit = int(s[j])
                freq[digit] += 1
                is_valid = all(num == 0 or num == freq[digit] for num in freq)
                if is_valid:
                    curr_hash = (hash_value[j + 1] - hash_value[i] * powers[j - i + 1] + mod * mod) % mod
                    ans.add(curr_hash)
        return len(ans)