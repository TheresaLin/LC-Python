# 31. Partition Array:把小於k放左邊，大於k放右邊
# time:O(N), space:O(1)

from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partition_array(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        # 如果用left < right，循環會在left == right的時候結束
        # 用left <= right會省去判斷nums[left]是<k or >= k
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left