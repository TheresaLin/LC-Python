# 26. Remove Duplicates from Sorted Array
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # record how many duplicates
        duplicate = 0
        for i in range(len(nums)):
            # when find the duplicate, duplicate+1
            if nums[i] == nums[i - 1]:
                duplicate += 1
            # when find the unique value, store to nums[i - duplicate]
            else:
                nums[i - duplicate] = nums[i]

        # return the number of unique value
        return len(nums) - duplicate