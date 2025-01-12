class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        open_char = []
        modified = []
        if len(s) % 2 == 1:
            return False
        for i in range(len(s)):
            if locked[i] == '0':
                modified.append(i)
            elif s[i] == '(':
                open_char.append(i)
            elif s[i] == ')':
                if open_char:
                    open_char.pop()
                elif modified:
                    modified.pop()
                else:
                    return False

        while modified and open_char and open_char[-1] < modified[-1]:
            modified.pop()
            open_char.pop()
        if open_char:
            return False
        return True       