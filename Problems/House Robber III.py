class Solution:
    def rob(self, root) -> int:
        def helper(node):
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return [rob, not_rob]

        return max(helper(root))