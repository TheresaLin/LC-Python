# 283. Move Zeroes
# Time complexity: O(n). Our fast pointer does not visit the same spot twice.
# Space complexity: O(1). All operations are made in-place

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        slow = 0

        for fast in range(len(nums)):
            # if slow pointer meets 0 and fast pointer meets non 0, then swip
            # because we want 0 go to the right side
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            
            # when slow pointer meets non 0 then keep going
            if nums[slow] != 0:
                slow += 1
            