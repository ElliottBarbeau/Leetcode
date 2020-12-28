class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    helper(root, sum, [], allPaths)
    return allPaths

def helper(root, sum, path, allPaths):
    if not root:
        return

    path.append(root.val)
    
    if root.val == sum and not root.left and not root.right:
        allPaths.append(list(path))
    
    else:  
        helper(root.left, sum - root.val, path, allPaths)
        helper(root.right, sum - root.val, path, allPaths)

    del path[-1]

def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))

main()
