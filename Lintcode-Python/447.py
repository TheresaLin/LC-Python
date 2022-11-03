# 447. Search in a Big Sorted Array
# Time: O(logK), Space: O(1)

class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # 初始化查找的範圍
        range_total = 1
        # 倍增法：如果target在查找範圍內，查找範圍倍增，時間複雜度為O(logK)
        while reader.get(range_total - 1) < target:
            range_total = range_total * 2

        # binary search模板
        start, end = 0, range_total - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) < target:
                start = mid
            elif reader.get(mid) > target:
                end = mid
            else:
                end = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1