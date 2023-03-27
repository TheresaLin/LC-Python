# 2583. Kth Largest Sum in a Binary Tree 
# 找加總k大的層
# BFS, TC:O(n), SC: O(n)
# 用deque做queue時間複雜度比較好



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        ans = []
        while q:
            count = 0

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                count += node.val
            ans.append(count)

        ans.sort()
        if k > len(ans):
            return -1
        return ans[-k]
                    