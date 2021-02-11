# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        arr = []
        self.helper(root, target, K, arr)
        return arr

    def helper(self, root, target, K, arr):
        if not root:
            return
        if root == target:
            self.findNodes(root, K, arr, -1)
        if root.right:
            self.helper(root.right, target, K, arr)
        if root.left:
            self.helper(root.left, target, K, arr)
    
    
    def findNodes(self, root, K, arr, dist):
        dist += 1
        if dist == K:
            arr.append(root.val)
            return
        if root.right:
            self.findNodes(root.right, K, arr, dist)
        if root.left:
            self.findNodes(root.left, K, arr, dist)
        