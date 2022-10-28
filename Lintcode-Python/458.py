# 458. Last Position of Target
# 學會模板就很容易

from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def last_position(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            # when nums[mid] == target, start should be mid
            else:
                start = mid
        # 因為是last postition，所以先放nums[end] == target
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1