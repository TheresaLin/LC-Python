# 75. Find Peak Element
# 有很多山峰，找出任一一個即可

from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        start, end = 1, len(a) - 2
        while start + 1 < end:
            mid = (start + end) // 2
            # mid跟前後數比較
            # mid比前面一位小，表示山峰在左邊，end = mid
            if a[mid] < a[mid - 1]:
                end = mid
            # mid比後面一位小，表示山峰在右邊，start = mid
            elif a[mid] < a[mid + 1]:
                start = mid
            # mid比前後都大，mid是山峰peak
            else:
                return mid
        # 因為保證有peak，start end選一個
        return end if a[start] < a[end] else start   