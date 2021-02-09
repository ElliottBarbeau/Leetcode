# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        order = []
        
        def inorder(root, order):
            stack = []
            while True:
                while root:
                    stack.append(root)
                    root = root.left
                if not stack:
                    return True
                node = stack.pop()
                if order and node.val <= order[-1]:
                    return False
                order.append(node.val)
                root = node.right
                
        return inorder(root, order)