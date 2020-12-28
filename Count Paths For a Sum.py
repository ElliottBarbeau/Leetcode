class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return helper(root, S, [])

def helper(current, target_sum, currentPath):
    if not current:
        return 0

    foundPath = 0
    currentPath.append(current.val)

    currSum = 0
    for i in reversed(range(len(currentPath))):
        currSum += currentPath[i]
        if currSum == target_sum:
            foundPath += 1

    foundPath += helper(current.left, target_sum, currentPath)
    foundPath += helper(current.right, target_sum, currentPath)

    del(currentPath[-1])

    return foundPath

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
