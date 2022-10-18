# 5. Kth Largest Element
# use quick select (similar to quick sort, but need to know whether k is less than rightindex or larger than leftindex)
class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kth_largest_element(self, k: int, nums: List[int]) -> int:
        # write your code here
        n = len(nums)
        
        # 為了方便，把第k大換成k小
        k = n - k
        if not nums:
            return -1
        return self.quick_select(nums, 0, n - 1, k)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
        left, right = start, end
        # 找中心點
        mid = nums[(start + end) // 2]
        # 方法跟quick sort很像
        while left <= right:
            # 先把nums[left] < mid都跳過，直到找到nums[left] > mid
            while left <= right and nums[left] < mid:
                left += 1
            # 先把nums[right] > mid都跳過，直到找到nums[right] < mid
            while left <= right and nums[right] > mid:
                right -= 1
            # 把找到的nums[left] > mid和nums[right] < mid對調
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # 假如k小在右側就搜索右側的範圍，否則搜索左側
        if k  <= right:
            return self.quick_select(nums, start, right, k)
        if k  >= left:
            return self.quick_select(nums, left,  end, k)
        return nums[k]
