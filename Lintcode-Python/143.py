# 143. Sort Colors II


from typing import (
    List,
)

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):

        if not colors or len(colors) < 2:
            return

        self.sort(colors, 1, k, 0, len(colors) - 1)

    # 遞歸三要素之一：遞歸的定義
    def sort(self, colors, color_from, color_to, left, right):
        # 遞歸三要素之三：遞歸的出口
        if color_from == color_to:
            return
        # 遞歸三要素之二：遞歸的分解
        mid_color = (color_from + color_to) // 2
        
        # 分區，左邊區域 <= 中間色，右邊 > 中間色
        while left <= right:
            while left <= right and colors[left] <= mid_color:
                left += 1
            while left <= right and colors[right] > mid_color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        # 左邊的分區：
        # 顏色區塊的起始位置為：color_from到mid_color
        # index則是從0到right，因爲在最後交換位置後，right-1 left+1，right會跑到left左邊
        self.sort(colors, color_from, mid_color, 0, right)
        # 右邊的分區
        self.sort(colors, mid_color + 1, color_to, left, len(colors) - 1)