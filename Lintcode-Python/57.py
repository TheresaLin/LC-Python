# 57. 3Sum
## 找三數加起來為零
## 此題用的是拿出小數，把小數導為負數變成target，然後找中數+大數＝target，相當於升級版twoSum

from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        # write your code here
        results = []
        # 找三數，length至少要大於等於3
        if not numbers or len(numbers) < 3:
            return results
        # use two pointers to find twoSum, need to use sort list
        numbers.sort()
        # 找小數
        for i in range(len(numbers) - 2):
            # 假如小數和上一位相同就跳過，否則會重複
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            # 中數的指針left, 大數的指針right, target = -小數
            left = i + 1
            right = len(numbers) - 1
            target = -numbers[i]
            self.twoSum(numbers, left, right, target, results)
        return results

        
    def twoSum(self, numbers, left, right, target, results):
        while left < right:
            if numbers[left] + numbers[right] == target:
                results.append([-target, numbers[left], numbers[right]])
                left += 1
                right -= 1
                # 排除中數和大數的重複值
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else: 
                left += 1
                