# # 148. Sort Colors

from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        if not nums:
            return
        
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, nums, start, end):
        if start >= end:
            return 
        left, right = start, end
        # 1. 需要訂一個中心點pivot, 取value而非index
        pivot = nums[(left + right) // 2]

        # 2. left <= right instead of <
        while left <= right:
            # 3. a[left] < pivot instead of <= 
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 退出循環後，left本來在左邊現在到右邊，right也是從右邊到左邊
        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)

sol = Solution()
print(sol.sort_colors([0,1,2,0,2,1,1,1,0,2,1,1,2,2,2,1]))