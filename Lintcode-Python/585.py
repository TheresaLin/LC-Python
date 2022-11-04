# 585. Maximum Number in Mountain Sequence

from typing import (
    List,
)

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountain_sequence(self, nums: List[int]) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # mid + 1 一定不會越界，因為 while start + 1 < end
            # start < mid + 1 < end
            # 如果nums[mid] > nums[mid + 1]代表越右邊數字越小越往下傾斜，山峰在左邊，丟掉右邊
            if nums[mid] > nums[mid + 1]:
                end = mid
            # 如果nums[mid]越右邊數字越大越往上爬升山峰在右邊，丟掉左邊
            else:
                start = mid
        # 比較start和end中較大的值，則為山頂
        return max(nums[start], nums[end])
