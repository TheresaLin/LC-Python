# 480. Binary Tree Paths

from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
             we will sort your return value in output
    """
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = []
        self.findPath(root, [root], paths)
        return paths

    def findPath(self, node, path, paths):
        if not node:
            return

        if not node.left and not node.right:
            paths.append("->".join([str(n.val) for n in path]))
            return
        
        path.append(node.left)
        self.findPath(node.left, path, paths)
        path.pop() # this is backtracking for variable path

        path.append(node.right)
        self.findPath(node.right, path, paths)
        path.pop() # this is backtracking for variable path