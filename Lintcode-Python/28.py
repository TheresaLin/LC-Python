# 28. Search a 2D Matrix
# 此題有兩種解法
# 解法一：row and column都做binaey search，先把找出target會在哪個row裡面，再找target在哪個column，找到return True 沒有找到return false。
# Time: O(logR + logC)Row二分 Column二分, Space: O(1)

from typing import (
    List,
)

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:

        # 確認target會是在第幾row行，若沒找到行座標， return -1
        row_index = self.find_row_index(matrix, target)
        if row_index == -1:
            return False
        # 在row裡面尋找target
        return self.find_target_in_row(matrix[row_index], target)

    # 第一層檢查，是否target在某row裡，用二分查找target是否在row[0]~row[col_cnt - 1]
    def find_row_index(self, matrix, target):
        row_cnt = len(matrix)
        col_cnt = len(matrix[0])

        start = 0
        end = row_cnt - 1

        while start + 1 < end:
            mid = (start + end) // 2
            mid_row = matrix[mid]
            # 發現在上半區間，捨去下半區
            if target < mid_row[0]:
                end = mid
            # 發現在下半區間，捨去上半區
            elif target > mid_row[col_cnt - 1]:
                start = mid
            # 找到行座標，return mid
            # mid_row[0] <= target <= mid_row[col_cnt - 1]
            else:
                return mid
        # 看會不會在start 或 end
        if matrix[start][0] <= target <= matrix[start][col_cnt - 1]:
            return start
        if matrix[end][0] <= target <= matrix[end][col_cnt - 1]:
            return end
        # 沒找到return -1
        return -1

    # 如果本行包含target，return True
    def find_target_in_row(self, row, target):
        start = 0
        end = len(row) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            # row[mid] < target，代表target在mid右邊，捨棄左邊
            if row[mid] < target:
                start = mid
            # row[mid] > target，代表target在mid左邊，捨棄右邊
            elif row[mid] > target:
                end = mid
            # row[mid] == target, return True
            else:
                return True
        # 看會不會在start 或 end
        return row[start] == target or row[end] == target 


# 解法二：把matrix換成array，二為換成一維
# 一維座標 = row index * num of row + column index
# ex: 3*4 的 matrix 求[1,1]--> 1 * 4 + 1 = 5
# 所以如果一維座標5要轉換成二維座標 
# row_index = 5 // 4 = 1, col_index = 5 % 4 = 1, 轉換成二維為[1, 1]
# Time: O(logRC) = O(logR + logC), Space: O(1)

from typing import (
    List,
)

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        # 二維坐標轉換為一維
        end = len(matrix) * len(matrix[0]) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            mid_value = self.get_mid_value(matrix, mid)
            if target < mid_value:
                end = mid
            elif target > mid_value:
                start = mid
            else:
                return True
        return self.get_mid_value(matrix, start) == target or \
               self.get_mid_value(matrix, end) == target

    # 一維轉換二維
    def get_mid_value(self, matrix, mid):
        col_cnt = len(matrix[0])
        # 算第幾行第幾列
        row_index = mid // col_cnt
        col_index = mid % col_cnt
        # 直接return value
        return matrix[row_index][col_index]

