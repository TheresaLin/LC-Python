# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 這題思考方式是recursion遞歸(很像for迴圈的function版): 1.return為結束點 2.回call function 3.每一層要做的事
# 在這題之中
# 1. 結束點為root == None
# 2. 每一層要做的事是找左節點和右節點的最大深度
# 3. 每一層要回傳給上層最大深度 + 1
# 先看[3,9,20], 3=root, 9為left, 20為right, 回傳的是left和right比較過後的最大深度，回傳每次都會在加1，這樣每一層才會都加1
#
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0        
        leftMax = self.maxDepth(root.left)  
        rightMax = self.maxDepth(root.right)
        return max(leftMax, rightMax)+1     