# 此題目的要了解如何使用適當的資料結構
# 首先創一個dictionary型態的NumFre存某數出現的次數
# 再把只出現一次的放進res[]最後查裡面的最大值
# 如果都沒有只出現一次的，return-1
 
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        if len(A) == 1:
            return A[0]
        NumFre = {}
        for i in A:
            if i not in NumFre:
                NumFre[i] = 1
            else:
                NumFre[i] = NumFre[i] + 1
        
        res = []
        for i in NumFre:
            if NumFre[i] == 1:
                res.append(i)
        
        if len(res) == 0:
            return -1
        else:
            return max(res)
        


# python的collections裡有Counter()可以直接以dictionary的型態存好某數出現的次數

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        if len(A) == 1:
            return A[0]
        NumFre = collections.Counter(A)
        
        res = []
        for i in NumFre:
            if NumFre[i] == 1:
                res.append(i)
        
        if len(res) == 0:
            return -1
        else:
            return max(res)