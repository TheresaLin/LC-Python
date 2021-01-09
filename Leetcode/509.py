# 注意return什麼
# f每次都會新增一個單位
class Solution:
    def fib(self, n: int) -> int:
        f = [0,1]
        for i in range(2, n+1):
            f.append(0)
            f[i] = f[i-1] + f[i-2]
            
        return f[n]


# 注意f的size只有2，他沒有新增空間，只會存在f[0]和f[1]裡面
# 此方法用的是滾動數組，就是只會存要的那三個空間
class Solution:
    def fib(self, n: int) -> int:
        f = [0,1]
        for i in range(2, n+1):
            f[i%2] = f[0] + f[1]
            
        return f[n%2]

# 此方法是用recursion
# 一開始就要用if return 最基本的case

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        f = self.fib(n-2) + self.fib(n-1)
        return f