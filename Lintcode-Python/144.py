# 144. Interleaving Positive and Negative Numbers
# 正負數交錯

from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, a: List[int]):
        if not a:
            return
        # 正負數的個數決定兩邊交換的起始點
        neg_cnt = self.partition(a)
        pos_cnt = len(a) - neg_cnt
        # 負比正多，起始點為1。跟正一樣多或比正少，起始點則為0
        left = 1 if neg_cnt > pos_cnt else 0
        # 正比負多，起始點為len(a)-2。跟負一樣多或比負少，起始點則為len(a)-1
        right = len(a) - (2 if pos_cnt > neg_cnt else 1)
        # call正負交錯的function
        self.interleave(a, left, right)

    # 簡單partition，把負放左正放右
    def partition(self, a):
        left, right = 0, len(a) - 1
        while left <= right:
            # 在左邊找正
            while left <= right and a[left] < 0:
                left += 1
            # 在右邊找負
            while left <= right and a[right] >= 0:
                right -= 1
            # 進行交換
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
        # 剛好left會於第一個正數index，且等於負數的個數
        return left

    def interleave(self, a, left, right):
        while left < right:
            a[left], a[right] = a[right], a[left]
            # 間隔交換，所以是+-2
            left += 2
            right -= 2

