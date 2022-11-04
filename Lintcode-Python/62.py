# 62. Search in Rotated Sorted Array
# 這題想法很跳躍


from typing import (
    List,
)

class Solution:
    """
    @param a: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, a: List[int], target: int) -> int:
        if not a:
            return -1
        start, end = 0, len(a) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            # mid在左上方的線，起點在右邊
            if a[mid] > a[end]:
                # 此時再判斷target是否在start和mid之間，有的話end=mid
                # target在中段
                if a[start] <= target <= a[mid]:
                    end = mid
                # target在頭段或尾段
                else:
                    start = mid

            # mid在右下方的線，起點在左邊
            else:
                # target在中段
                if a[mid] <= target <= a[end]:
                    start = mid
                # target在頭段或尾段
                else:
                    end = mid
        if a[start] == target:
            return start
        if a[end] == target:
            return end
        return -1   
    
