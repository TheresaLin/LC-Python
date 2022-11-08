# 183. Wood Cut 是很難的一題
# 題目：有多根木頭要進行整數切割，最後要獲得k段等長的木頭（木頭不能拼接），切割後木頭的最大長度應為多少
# 是一題負相關的映射關係
# Time: O(KlogN) K=原木段數, N=答案範圍大小
# Space: O(1)

from typing import (
    List,
)

class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def wood_cut(self, l: List[int], k: int) -> int:
        # write your code here
        if not l:
            return 0

        # 切割長度, end = min(l裡面最大值和平均)
        start, end = 1, min(max(l), sum(l) // k)

        # 如果end < 1，則不可能完成任務
        if end < 1:
            return 0

        while start + 1 < end:
            mid = (start + end) // 2
            # 長度為mid的切塊木頭總數 >= k，則繼續增加木頭長度，選右邊
            if self.get_count(l, mid) >= k:
                start = mid
            # 長度為mid的切塊木頭總數 < k，則繼續縮短木頭長度，選左邊
            else:
                end = mid
        # 因為排除無解狀況，所以一定有解，非end即start
        # 如果end符合要求首選end(因為end更長)，否則選start
        return end if self.get_count(l, end) >= k else start

    def get_count(self, l, mid):
        # 把所有木頭切mid長度，加總起來得總段數
        return sum(i // mid for i in l)