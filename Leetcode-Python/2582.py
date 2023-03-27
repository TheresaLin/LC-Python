# 2582. Pass the Pillow 

# Greedy TC:O(1), SC:O(1)
# rounds --> 計算來回繞幾輪，如果是偶數輪代表是正著數，奇數輪則是倒著數
# nums --> 計算餘數

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds = time // (n - 1)
        nums = time % (n - 1)
        if rounds % 2 == 0:
            return nums + 1
        return n - nums

sol = Solution()
print(sol.passThePillow(18, 38))