# 80. Median
# use quick select(concept is same as 5.py)

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return    
        med = (len(nums) - 1) // 2
        print(med)
        return self.quick_select(nums, 0, len(nums) - 1, med)

    def quick_select(self, nums, start, end, med):
        left, right = start, end
        pivot = nums[(left + right) // 2]
        if start == end:
            return nums[start]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # print(nums, start, right, N)
        if med <= right:
            return self.quick_select(nums, start, right, med)
        if med >= left:
            return self.quick_select(nums, left, end, med)
        return nums[med]
