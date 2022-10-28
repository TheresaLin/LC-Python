## 457. Classical Binary Search

### Recursion
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        return self.binarySearch(nums, 0, len(nums) - 1, target)


        
    def binarySearch(self, nums, start, end, target):
        # when the pointer doesn't find the target number
        if start > end:
            return -1
        
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        ## when nums[mid] < target means target is in the right, so search the area of "mid+1 to end"
        if nums[mid] < target:
            return self.binarySearch(nums, mid + 1, end, target)

        return self.binarySearch(nums, start + 1, mid, target)



### 二分法
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        # 用 start + 1 < end 而不是 start < end 的目的是为了避免死循环
        while start + 1 < end:
            mid = (start + end) // 2
            # > , =, < 的逻辑先分开写，然后在看看 = 的情况是否能合并到其他分支里
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        # 需要再单独判断 start 和 end 这两个数谁是我们要的答案
        # 如果是找 first position of target 就先看 start，否则就先看 end
        if nums[start] == target:
                return start
        if nums[end] == target:
                return end
        return -1