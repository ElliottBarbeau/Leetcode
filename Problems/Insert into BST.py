class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        self.helper(root, val)
        return root

    def helper(self, root, val):
        if val > root.val:
            if root.right:
                self.helper(root.right, val)
            else:
                root.right = TreeNode(val)
                return
        else:
            if root.left:
                self.helper(root.left, val)
            else:
                root.left = TreeNode(val)
                return