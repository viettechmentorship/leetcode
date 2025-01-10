class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cnt_word2 = [0] * 26
        for word in words2:
            curr_cnt = Counter(word)
            for i in range(len(word)):
                char = word[i]
                cnt_word2[ord(char) - 97] = max(cnt_word2[ord(char) - 97], curr_cnt[char])
        
        ans = []
        for word in words1:
            cnt = Counter(word)
            is_universal = True
            for i in range(26):
                if cnt.get(chr(i + 97), 0) < cnt_word2[i]:
                    is_universal = False
                    break
            if is_universal:
                ans.append(word)
        return ans