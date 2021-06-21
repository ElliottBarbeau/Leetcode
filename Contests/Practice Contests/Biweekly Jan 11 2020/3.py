# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.dfs(root, None, None)
        return self.s
    
    def dfs(self, node, parent, grandparent):
        if not node:
            return
        
        if grandparent and grandparent.val % 2 == 0:
            self.s += node.val
            
        self.dfs(node.left, node, parent)
        self.dfs(node.right, node, parent)