class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = [0] * (len(A) + 1)
        ans = [0] * (len(A))
        cnt = 0
        for i in range(len(A)):
            num1, num2 = A[i], B[i] 
            freq[num1] += 1 
            if freq[num1] == 2:
                cnt += 1
            freq[num2] += 1 
            if freq[num2] == 2:
                cnt += 1
            ans[i] = cnt
        return ans