#Recursive inorder traversal
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        l = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            l.append(node.val)
            if node.right:
                dfs(node.right)
            return l
        return dfs(root)

#Recursive preorder traversal
class Solution2:
    def preorderTraversal(self, root):j
        if not root:
            return []
        l = []
        def dfs(node):
            l.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            return l
        return dfs(root)

#Recursive postorder traversal
class Solution3:
    def postorderTraversal(self, root):
        if not root:
            return []
        l = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            l.append(node.val)
            return l
        return dfs(root)