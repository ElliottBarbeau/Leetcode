class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    if not root:
        return len(sequence) == 0
        
    return True if helper(root, sequence, 0) else False

def helper(root, sequence, depth):
    if not root or root.val != sequence[depth]:
        return

    if depth == len(sequence)-1 and root.val == sequence[depth]:
        return True

    return (helper(root.left, sequence, depth + 1) or helper(root.right, sequence, depth + 1))


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
