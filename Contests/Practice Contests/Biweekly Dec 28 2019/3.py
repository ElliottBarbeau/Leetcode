# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    score = 0
    def deepestLeavesSum(self, root: TreeNode) -> int:
        maxHeight = self.height(root)
        self.compute(root, 1, maxHeight)
        return self.score
        
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def compute(self, root, currHeight, maxHeight):
        if not root:
            return
        
        if currHeight == maxHeight:
            self.score += root.val
            
        self.compute(root.left, currHeight + 1, maxHeight)
        self.compute(root.right, currHeight + 1, maxHeight)
            
        