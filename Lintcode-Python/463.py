# 463 · Sort Integers

## quick sort: 取中心點整體有序再用遞歸做局部排序
class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers(self, a: List[int]):
        # write your code here
        if not a:
            return 
        self.quick_sort(a, 0, len(a) - 1)

    def quick_sort(self, a, start, end):
        if start >= end:
            return 
        left, right = start, end
        # 1. 需要訂一個中心點pivot, 取value而非index
        pivot = a[(left + right) // 2]

        # 2. left <= right instead of <
        while left <= right:
            # 3. a[left] < pivot instead of <= 
            while left <= right and a[left] < pivot:
                left += 1
            while left <= right and a[right] > pivot:
                right -= 1
            if left <= right:
                temp = a[left]
                a[left] = a[right]
                a[right] = temp
                left += 1
                right -= 1

        self.quick_sort(a, start, right)
        self.quick_sort(a, left, end)


