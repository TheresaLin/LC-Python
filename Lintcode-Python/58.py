# 58. 4Sum
# 排序後把最小的兩個數用for迴圈固定，target-兩最小數之後就為指針left, right的twoSum_target

from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
             we will sort your return value in output
    """
    def four_sum(self, numbers: List[int], target: int) -> List[List[int]]:
        if not numbers and len(numbers) < 4:
            return []

        results = []
        numbers.sort()
        # i, j為四數中最小的兩數index
        for i in range(len(numbers) - 4):
            # 最小數與前一位數相同則跳過
            if i > 0 and numbers[i] == numbers[i - 1]:
                    continue
            # j為第二小數的index
            for j in range(i + 1, len(numbers) - 3):
                # 第二小數與前一位數相同則跳過
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                twoSum_target = target - numbers[i] - numbers[j]
                # left為第二大數，等同於第三小數
                left = j + 1
                # right為最大數
                right = len(numbers) - 1
                self.twoSum(numbers, i, j, left, right, twoSum_target, results)
        return results
    
    def twoSum(self, numbers, i, j, left, right, target, results):
        while left < right:
            if numbers[left] + numbers[right] == target:
                results.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                left += 1
                right -= 1
                # 跳過第二大數和最大數的重複值問題
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1








