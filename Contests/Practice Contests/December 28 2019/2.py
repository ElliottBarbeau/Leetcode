# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        t1 = []
        t2 = []
        ans = []
        self.inorder(root1, t1)
        self.inorder(root2, t2)
        t1p, t2p = 0, 0
        while t1p < len(t1) and t2p < len(t2):
            if t1[t1p] < t2[t2p]:
                ans.append(t1[t1p])
                t1p += 1
            else:
                ans.append(t2[t2p])
                t2p += 1

        if t1p == len(t1):
            ans += t2[t2p:]
        else:
            ans += t1[t1p:]

        return ans
        
    def inorder(self, root, a):
        if not root:
            return
        self.inorder(root.left, a)
        a.append(root.val)
        self.inorder(root.right, a)