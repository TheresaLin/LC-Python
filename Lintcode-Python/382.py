# 382. Triangle Count

from typing import (
    List,
)

class Solution:
    """
    @param s: A list of integers
    @return: An integer
    """
    def triangle_count(self, s: List[int]) -> int:
        # write your code here
        if not s or len(s) < 3:
            return 0
        # 因為題目問的是有幾組且可重複，所以答案只要記下有幾組就行
        ans = 0
        s.sort()
        # 找大數並設為target，並且把小數和中數的index傳給function
        for i in range(2, len(s)):
            left = 0
            right = i - 1
            target = s[i]
            ans += self.get_triangle_count(s, left, right, target)
        return ans

    def get_triangle_count(self, s, left, right, target):
        # 每一層大邊回傳的組合數
        cnt = 0
        while left < right:
            # 三角形定律：兩小邊相加要大於大邊
            if s[left] + s[right] > target:
                # 若發現小＋中邊已大於大邊，表示中邊到小邊的組合都可行
                cnt += right - left
                right -= 1
            else:
                left += 1
        return cnt

