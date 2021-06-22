# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        return self.postorder(root, target)
        
    def postorder(self, root, target):
        if not root:
            return
        
        root.left = self.postorder(root.left, target)
        root.right = self.postorder(root.right, target)
            
        if not root.left and not root.right and root.val == target:
            return None
        else:
            return root
            