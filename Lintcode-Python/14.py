## 14. First Position of Target


from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binary_search(self, nums: List[int], target: int) -> int:
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
            # when nums[mid] == target, end should be mid
            else:
                end = mid
        # 因為是first postition，所以先放nums[end] == target
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
