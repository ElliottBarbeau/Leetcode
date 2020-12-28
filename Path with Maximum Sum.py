import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaximumPathSum:
    def find_maximum_path_sum(self, root):
        self.globalMaximum = float('-inf')
        self.find_maximum_sum(root)
        return self.globalMaximum

    def find_maximum_sum(self, current):
        if not current:
            return 0

        maxFromLeft = self.find_maximum_sum(current.left)
        maxFromRight = self.find_maximum_sum(current.right)

        m = maxFromLeft + maxFromRight + current.val

        self.globalMaximum = max(self.globalMaximum, m)

        return max(maxFromLeft, maxFromRight) + current.val


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(MaximumPathSum().find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(MaximumPathSum().find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(MaximumPathSum().find_maximum_path_sum(root)))


main()
