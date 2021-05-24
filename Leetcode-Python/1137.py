# 注意 index out of range
# 所以要先設置空間k.append(0)在加數據之前


class Solution:
    def tribonacci(self, n: int) -> int:
        k = [0, 1, 1]
        for i in range(3, n+1): # range(start, end): start ~ end-1 / range(end): 0 ~ end-1
            k.append(0)
            k[i] = k[i-3] + k[i-2] + k[i-1]
        return k[n]




# 優化空間版本
# 此方法用的是滾動數組，就是只會存要的那三個空間
class Solution:
    def tribonacci(self, n: int) -> int:
        k = [0, 1, 1]
        for i in range(3, n+1):
            t = i%3
            k[t] = sum(k)
        return k[n%3]