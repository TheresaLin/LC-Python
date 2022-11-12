# 86. Binary Search Tree Iterator
# hard!!要你寫class裡面的函數，要用非帝圭的方式實現二叉數遍歷，用DFS的中序遍歷
# 有兩種解法，請把解法二倒背如流


## 解法一

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        # root非空就要一直往左子樹下挖
        while root != None:
            self.stack.append(root)
            root = root.left
    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # 當stack為空，表示沒有next node
        return len(self.stack) > 0
    """
    @return: return next node
    """
    def _next(self):
        # 拿出尾巴
        node = self.stack[-1]
        # 若右子數非空
        if node.right is not None:
            n = node.right
            # 在右子數非空的情況下，右子數往左邊走的所有節點記錄下來
            while n != None:
                self.stack.append(n)
                n = n.left
        # 若為空，ㄧ路pop到是左子樹關係
        else:  
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()

        return node



## 解法二：更簡易，在stack不保留已經被訪問過的節點
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        # root非空就要一直往左子樹下挖
        self.find_most_left(root)

    def find_most_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # 當stack為空，表示沒有next node
        return bool(self.stack)
    """
    @return: return next node
    """
    def _next(self):
        # 直接pop
        node = self.stack.pop
        # 若右子數非空
        if node.right:
            self.find_most_left(node.right)
        return node