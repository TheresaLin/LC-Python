# 633. Sum of Square Numbers
# 最大的數就開根號target的數然後取整數

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        while left <= right:
            if left * left + right * right == c:
                return True
            if left * left + right * right < c:
                left += 1
            if left * left + right * right > c:
                right -= 1
        return False