# 暴力破解
# 注意i和j不能為同一個位置

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if target == nums[i] + nums[j]:
                        return [i, j]

# 暴力破解簡化版
# j直接從i之後開始檢查，所以不會有i和j同一個位置的情況
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 優化解法
# dic裡面的key為target-當前位置的數， value為當前位置
# 找到跟key相同的數就回傳，相同key的位置和當前位置

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            dic[target-nums[i]] = i