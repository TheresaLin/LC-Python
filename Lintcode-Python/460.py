# 460. Find K Closest Elements

# Time: O(logN) + O(K)，二分法binary search找target需要O(logN)，merge過程需要O(K)
# Space: O(K)


from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        # 找最接近target的右邊index和左邊index
        right = self.findRightClosest(a, target)
        left = right - 1
        results = []
        # 兩指針向外擴張找出最接近的target的k個數
        for _ in range(k):
            # 若左邊更接近target選左邊
            if self.isLeftColser(a, target, left, right):
                results.append(a[left])
                # 注意！因為他是最靠近target的左邊，所以指針要再向左擴張，所以-1
                left -= 1

            # 若右邊更靠近target選右邊
            else:
                results.append(a[right])
                right += 1
        return results

    # 回傳True-->選左邊; False-->選右邊
    def isLeftColser(self, a, target, left, right):
        # left若已經到底了，返回flase，讓results.append右邊
        if left < 0:
            return False
        # right若已經到底了，返回true，讓results.append左邊
        if right == len(a):
            return True
        # 如果左右與target的距離相等選左邊，abs()取絕對值
        return abs(target - a[left]) <= abs(target - a[right])

    # 找出最接近target右邊（>= target）的index
    def findRightClosest(self, a, target):
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] < target:
                start = mid
            if a[mid] >= target:
                end = mid

        # 注意：除了等於要加上大於 target，因為有可能list沒有此數
        if a[start] >= target:
            return start
        if a[end] >= target:
            return end

        # 都沒找到的情況，代表target大於list裡面的最大值
        # 因此把target定義為在最右邊，後續的results只會往左邊append
        return len(a)