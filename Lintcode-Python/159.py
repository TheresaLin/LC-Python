# 159. Find Minimum in Rotated Sorted Array
# 此題思維很特別，從排序過的數據切一刀，把右邊換到左邊 ex: [4,5,6,7,1,2,3]
# 要判斷是放棄mid右邊還是左邊，先把mid直接跟數據最尾端的3做比較
# 假如是>mid代表mid是在[4,5,6,7]那一段，所以放棄左邊，反之放棄右邊
from typing import (
    List,
)

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums: List[int]) -> int:
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # nums[mid] < nums[end] 代表起點在左邊，拋棄右邊
            if nums[mid] < nums[end]:
                end = mid
            # nums[mid] > nums[end] 代表起點在右邊，拋棄左邊
            # 因為沒有重複值，所以不會有等於，所以這邊else: nums[mid] > nums[end]
            else:
                start = mid
        return min(nums[start], nums[end])
