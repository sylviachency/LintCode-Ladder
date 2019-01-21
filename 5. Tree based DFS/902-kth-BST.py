"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        self.kth = k
        self.result = 0
        
        self.DFS(root)
        return self.result
        
    def DFS(self, root):
        if not root:
            return 0
            
        self.DFS(root.left)
        self.kth -= 1 
        if self.kth == 0:
            self.result = root.val
        self.DFS(root.right)
        
        