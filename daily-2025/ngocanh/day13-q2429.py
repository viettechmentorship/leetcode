"""
0011 - x
0001 - num1
0010
"""
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ans = num1
        bit_ans = bin(ans).count('1')
        bit_num2 = bin(num2).count('1')

        if bit_ans < bit_num2:
            for i in range(32):
                if bit_ans == bit_num2:
                    break
                
                # the ith bit is 0
                if ans & (1 << i) == 0: 
                    ans |= (1 << i)
                    bit_ans += 1
        elif bit_ans > bit_num2:
            for i in range(32):
                if bit_ans == bit_num2:
                    break
                
                # the ith bit is 1
                if ans & (1 << i) != 0:
                    ans ^= (1 << i)
                    bit_ans -= 1
        return ans