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

        # 退出循環後，left本來在左邊現在到右邊，right也是從右邊到左邊
        self.quick_sort(a, start, right)
        self.quick_sort(a, left, end)


## merge sort: 取中心點整體有序再用遞歸做局部排序，在做局部排序的時候，兩個指針都是同向進行

class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers(self, a: List[int]):
        # write your code here
        if not a:
            return 
        # temp 是在merge排序過程中的暫時list，大小需要跟a list一樣
        temp = [0] * len(a)
        
        self.merge_sort(a, 0, len(a)-1, temp)

    def merge_sort(self, a, start, end, temp):
        if start >= end:
            return
        self.merge_sort(a, start, (start + end) // 2, temp)
        self.merge_sort(a, (start + end) // 2 + 1, end, temp)
        self.merge(a, start, end, temp)
    
    def merge(self, a, start, end, temp):
        middle = (start + end) // 2
        leftIndex = start
        rightIndex = middle +1
        index = leftIndex

        # 左邊的index在middle以內，右邊的index在end以內
        while leftIndex <= middle and rightIndex <= end:
            # 左邊比右邊小，左邊放進temp裡面，並且leftIndex++
            if a[leftIndex] < a[rightIndex]:
                temp[index] = a[leftIndex]
                leftIndex += 1
            # 右邊比左邊小，右邊放進temp裡面，並且rightIndex++
            else:
                temp[index] = a[rightIndex]
                rightIndex += 1
            # temp的index不管上述哪種情況都要++
            index += 1

        # 右邊的index已經找完的情況，
        while leftIndex <= middle:
            temp[index] = a[leftIndex]
            index += 1
            leftIndex += 1
        
        # 左邊的index已經找完的情況
        while rightIndex <= end:
            temp[index] = a[rightIndex]
            index += 1
            rightIndex += 1
        
        # 把temp的value放回a裡面
        for i in range(start, end + 1):
            a[i] = temp[i]


