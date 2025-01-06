class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        directions = [0] * (len(s))
        for start, end, dir in shifts:
            if dir == 1:
                directions[start] += 1
                if end + 1 < len(s):
                    directions[end + 1] -= 1
            else:
                directions[start] -= 1
                if end + 1 < len(s):
                    directions[end + 1] += 1
        for i in range(1, len(directions)):
            directions[i] = (directions[i] + directions[i - 1]) % 26
        s_arr = list(s)
        for i in range(len(s_arr)):
            curr = (ord(s_arr[i]) - 97 + directions[i]) % 26 + 97
            s_arr[i] = chr(curr)
        return "".join(s_arr)