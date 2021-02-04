from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = []
    left_to_right = 1

    queue = deque()
    queue.append(root)

    while queue:
        currentLevel = deque()
        levelSize = len(queue)

        for _ in range(levelSize):
            currentNode = queue.popleft()
            if left_to_right > 0:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        left_to_right *= -1
        result.append(list(currentLevel))

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
