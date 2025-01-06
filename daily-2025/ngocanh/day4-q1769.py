class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * (len(boxes))
        move_left, move_right, ball_left, ball_right = 0, 0, 0, 0
        for i in range(len(boxes)):
            ans[i] += move_left
            ball_left += int(boxes[i])
            move_left += ball_left
            j = len(boxes) - 1 - i
            ans[j] += move_right
            ball_right += int(boxes[j])
            move_right += ball_right
        return ans